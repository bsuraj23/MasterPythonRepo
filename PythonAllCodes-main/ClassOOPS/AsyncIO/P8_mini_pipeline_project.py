import asyncio
import random
from dataclasses import dataclass


@dataclass
class JobResult:
    job_id: int
    status: str
    value: int


class AsyncPipeline:
    def __init__(self, workers: int = 3, retries: int = 2) -> None:
        self.queue: asyncio.Queue[int | None] = asyncio.Queue()
        self.workers = workers
        self.retries = retries
        self.results: list[JobResult] = []
        self.lock = asyncio.Lock()

    async def produce(self, total_jobs: int) -> None:
        for job_id in range(1, total_jobs + 1):
            await self.queue.put(job_id)
            print(f"Queued job {job_id}")

        for _ in range(self.workers):
            await self.queue.put(None)

    async def process_one(self, job_id: int) -> JobResult:
        # Simulate unstable external work with random failures.
        if random.random() < 0.25:
            raise RuntimeError(f"Temporary failure on job {job_id}")

        await asyncio.sleep(random.uniform(0.2, 0.8))
        value = job_id * 10
        return JobResult(job_id=job_id, status="ok", value=value)

    async def process_with_retry(self, job_id: int) -> JobResult:
        attempt = 0
        while True:
            try:
                return await self.process_one(job_id)
            except RuntimeError as exc:
                attempt += 1
                if attempt > self.retries:
                    print(f"Job {job_id} failed after retries: {exc}")
                    return JobResult(job_id=job_id, status="failed", value=0)
                backoff = 0.2 * attempt
                print(f"Retrying job {job_id} in {backoff:.1f}s")
                await asyncio.sleep(backoff)

    async def worker(self, worker_name: str) -> None:
        while True:
            job_id = await self.queue.get()
            if job_id is None:
                self.queue.task_done()
                print(f"{worker_name} stopping")
                break

            result = await self.process_with_retry(job_id)
            async with self.lock:
                self.results.append(result)

            print(f"{worker_name} completed job {job_id} ({result.status})")
            self.queue.task_done()

    async def run(self, total_jobs: int) -> None:
        producer_task = asyncio.create_task(self.produce(total_jobs))
        worker_tasks = [
            asyncio.create_task(self.worker(f"worker-{idx}"))
            for idx in range(1, self.workers + 1)
        ]

        await asyncio.gather(producer_task)
        await self.queue.join()
        await asyncio.gather(*worker_tasks)

    def summary(self) -> None:
        ok_values = [item.value for item in self.results if item.status == "ok"]
        failed_count = sum(1 for item in self.results if item.status == "failed")

        print("\nPipeline Summary")
        print("-" * 30)
        print(f"Total jobs:   {len(self.results)}")
        print(f"Success jobs: {len(ok_values)}")
        print(f"Failed jobs:  {failed_count}")
        print(f"Total value:  {sum(ok_values)}")


async def main() -> None:
    random.seed(7)
    pipeline = AsyncPipeline(workers=3, retries=2)
    await pipeline.run(total_jobs=12)
    pipeline.summary()


if __name__ == "__main__":
    asyncio.run(main())
