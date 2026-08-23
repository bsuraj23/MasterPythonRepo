import asyncio


class AsyncOrderSystem:
    def __init__(self) -> None:
        self.queue: asyncio.Queue[int] = asyncio.Queue()

    async def producer(self, total_orders: int) -> None:
        for order_id in range(1, total_orders + 1):
            await asyncio.sleep(0.3)
            await self.queue.put(order_id)
            print(f"Produced order: {order_id}")

        await self.queue.put(-1)

    async def consumer(self) -> None:
        while True:
            order_id = await self.queue.get()
            if order_id == -1:
                self.queue.task_done()
                print("No more orders. Consumer stopping.")
                break

            print(f"Processing order: {order_id}")
            await asyncio.sleep(0.5)
            print(f"Completed order: {order_id}")
            self.queue.task_done()


async def main() -> None:
    system = AsyncOrderSystem()

    producer_task = asyncio.create_task(system.producer(total_orders=5))
    consumer_task = asyncio.create_task(system.consumer())

    await asyncio.gather(producer_task, consumer_task)


if __name__ == "__main__":
    asyncio.run(main())
