import asyncio
import random


class AsyncAPISimulator:
    def __init__(self, max_concurrent: int = 3) -> None:
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def call_api(self, request_id: int) -> str:
        async with self.semaphore:
            delay = random.uniform(0.8, 2.0)
            print(f"Request {request_id} started (delay={delay:.2f}s)")
            await asyncio.sleep(delay)
            print(f"Request {request_id} done")
            return f"response-{request_id}"


async def main() -> None:
    api = AsyncAPISimulator(max_concurrent=3)
    tasks = [asyncio.create_task(api.call_api(i)) for i in range(1, 11)]
    responses = await asyncio.gather(*tasks)
    print("All responses:", responses)


if __name__ == "__main__":
    asyncio.run(main())
