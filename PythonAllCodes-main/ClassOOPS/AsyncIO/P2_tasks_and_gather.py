import asyncio
import time


async def fetch_data(name: str, delay: int) -> str:
    print(f"{name}: started")
    await asyncio.sleep(delay)
    print(f"{name}: completed")
    return f"result-{name}"


async def main() -> None:
    start = time.perf_counter()

    task1 = asyncio.create_task(fetch_data("task-1", 2))
    task2 = asyncio.create_task(fetch_data("task-2", 1))
    task3 = asyncio.create_task(fetch_data("task-3", 3))

    results = await asyncio.gather(task1, task2, task3)

    end = time.perf_counter()
    print("Results:", results)
    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
