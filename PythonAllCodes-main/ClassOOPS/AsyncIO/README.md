# AsyncIO in Python (Beginner to Pro)

This folder is a progressive path to learn `asyncio` using simple and practical examples.

## Learning Order

1. `P1_async_intro.py`
   - What is a coroutine?
   - How `async` and `await` work

2. `P2_tasks_and_gather.py`
   - Running multiple tasks concurrently
   - Using `create_task()` and `gather()`

3. `P3_async_class_methods.py`
   - OOP with `async` methods
   - Concurrent execution inside class design

4. `P4_queue_producer_consumer.py`
   - Producer-consumer pattern with `asyncio.Queue`

5. `P5_timeout_and_cancellation.py`
   - Timeouts with `wait_for`
   - Graceful cancellation handling

6. `P6_semaphore_rate_limit.py`
   - Limiting concurrency with `Semaphore`

7. `P7_to_thread_bridge.py`
   - Mixing async code with blocking code using `asyncio.to_thread`

8. `P8_mini_pipeline_project.py`
   - End-to-end mini project with retries, queueing, worker pool, and aggregation

## Run a File

```bash
python P1_async_intro.py
```

Run files one by one in order.
