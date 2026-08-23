import asyncio
import time


def blocking_file_process(file_name: str) -> str:
    time.sleep(2)
    return f"Processed {file_name} in thread"


async def async_controller(file_name: str) -> str:
    print(f"Sending {file_name} to thread")
    result = await asyncio.to_thread(blocking_file_process, file_name)
    return result


async def main() -> None:
    tasks = [
        asyncio.create_task(async_controller("report_1.txt")),
        asyncio.create_task(async_controller("report_2.txt")),
        asyncio.create_task(async_controller("report_3.txt")),
    ]

    results = await asyncio.gather(*tasks)
    print("Results:")
    for item in results:
        print(item)


if __name__ == "__main__":
    asyncio.run(main())
