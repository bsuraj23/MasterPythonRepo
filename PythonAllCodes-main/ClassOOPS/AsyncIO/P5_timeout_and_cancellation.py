import asyncio


async def slow_task(name: str, delay: int) -> str:
    try:
        print(f"{name}: started")
        await asyncio.sleep(delay)
        print(f"{name}: completed")
        return f"{name}-ok"
    except asyncio.CancelledError:
        print(f"{name}: cancelled")
        raise


async def main() -> None:
    try:
        result = await asyncio.wait_for(slow_task("task-A", 4), timeout=2)
        print("Result:", result)
    except TimeoutError:
        print("Timeout happened for task-A")

    task_b = asyncio.create_task(slow_task("task-B", 5))
    await asyncio.sleep(1)
    task_b.cancel()

    try:
        await task_b
    except asyncio.CancelledError:
        print("Handled cancellation for task-B")


if __name__ == "__main__":
    asyncio.run(main())
