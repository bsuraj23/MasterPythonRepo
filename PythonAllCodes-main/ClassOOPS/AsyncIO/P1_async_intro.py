import asyncio


async def say_after(delay: int, message: str) -> None:
    await asyncio.sleep(delay)
    print(message)


async def main() -> None:
    print("Start")
    await say_after(1, "Hello")
    await say_after(1, "World")
    print("Done")


if __name__ == "__main__":
    asyncio.run(main())
