# Pending Changes Summary (uncommitted, as of 2026-08-23)

This documents the current uncommitted work sitting in the working tree on branch `main`:
2 modified files under `DataAbstractions/` and a new `AsyncIO/` module (9 files, all untracked).

## 1. Modified: `DataAbstractions/AbstractClass.py`

Existing content: a `Shape(ABC)` base class with a no-op `area()` method, subclassed by
`Rectangle`, demonstrating that Python raises `TypeError` if an abstract method isn't
implemented.

**New addition** (appended as comments, lines 24-25): a self-note explaining *why* `from abc
import ABC` is used — that `ABC` lets you define abstract base classes which can't be
instantiated directly and must be subclassed, enforcing an interface contract. This looks
like a personal learning note answering the question "why do we import ABC?", not functional
code.

## 2. Modified: `DataAbstractions/AbstractMethods.py`

Existing content: an abstract `Shape(ABC)` class with two `@abstractmethod`s, `perimeter()`
and `add()`.

**New addition**: an explanatory comment block, plus a new concrete `Circle(Shape)` subclass
that:
- stores a `radius`
- implements `perimeter()` as `2 * 3.14 * radius`
- implements `add()` to combine two `Circle` instances (raises `ValueError` if the other
  operand isn't a `Circle`)

This fulfills the pre-existing `#ADD more example code below` TODO in the file with a working
example of implementing an abstract class.

## 3. New: `AsyncIO/` folder (untracked, 9 files)

A self-contained, progressive `asyncio` tutorial series, each file runnable standalone via
`python P<N>_*.py`. A `README.md` inside the folder already documents the intended learning
order (reproduced/expanded below).

| File | Concept | What it demonstrates |
|---|---|---|
| `P1_async_intro.py` | Coroutine basics | `async`/`await`, `asyncio.sleep`, `asyncio.run` |
| `P2_tasks_and_gather.py` | Concurrency primitives | `create_task()` + `gather()` running 3 tasks concurrently, timed with `time.perf_counter` |
| `P3_async_class_methods.py` | Async OOP | A `@dataclass` (`AsyncStudentTask`) with an `async` method, orchestrated by an `AsyncClassroom` class that gathers multiple students' tasks |
| `P4_queue_producer_consumer.py` | Producer/consumer | `AsyncOrderSystem` uses `asyncio.Queue` with a producer and consumer coroutine, sentinel value (`-1`) to signal completion |
| `P5_timeout_and_cancellation.py` | Timeouts & cancellation | `asyncio.wait_for` with a timeout, manual `task.cancel()`, and handling `asyncio.CancelledError` |
| `P6_semaphore_rate_limit.py` | Concurrency limiting | `AsyncAPISimulator` uses `asyncio.Semaphore(3)` to cap concurrent "API calls" among 10 requests |
| `P7_to_thread_bridge.py` | Mixing sync/async | `asyncio.to_thread()` to run blocking (`time.sleep`) code without blocking the event loop |
| `P8_mini_pipeline_project.py` | Capstone project | `AsyncPipeline`: multi-worker queue processing with retry/backoff logic on random failures, `asyncio.Lock` for safe shared-state updates, and a final summary report |

### Progression logic
The series builds deliberately from fundamentals to a production-shaped pattern:
1. Single coroutine → 2. concurrent tasks → 3. async methods inside classes → 4. queue-based
coordination → 5. robustness (timeouts/cancellation) → 6. throttling → 7. bridging blocking
code → 8. combining all of the above (queue + workers + retries + locking) into one pipeline.

## Net effect

- Two small, low-risk documentation/example additions to existing OOP abstraction lessons.
- One complete new self-study module on Python `asyncio`, ready to commit as-is (README
  already present, files already follow a consistent style: type hints, `dataclass` usage,
  `if __name__ == "__main__":` entry points).
