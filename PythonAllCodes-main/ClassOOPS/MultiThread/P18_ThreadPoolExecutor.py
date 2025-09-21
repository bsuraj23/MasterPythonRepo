from concurrent.futures import ThreadPoolExecutor
import time

def pool_task(x):
    print(f"ThreadPool task {x}")
    time.sleep(0.5)
    return x * x

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(pool_task, range(5)))

print("ThreadPool results:", results)

# Additional example: Using ThreadPoolExecutor for I/O-bound tasks
def io_bound_task(n):
    print(f"Starting I/O-bound task {n}")
    time.sleep(1)  # Simulate I/O delay
    print(f"Completed I/O-bound task {n}")
    return f"Result of task {n}"
with ThreadPoolExecutor(max_workers=2) as executor:
    future_results = [executor.submit(io_bound_task, i) for i in range(4)]
    for future in future_results:
        print(future.result())
    consumer_thread.join()
consumer_thread.join()
# Example of ThreadPoolExecutor in a class method

class ThreadPoolExample:
    def __init__(self, max_workers=2):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def run_tasks(self, tasks):
        futures = [self.executor.submit(self.task, t) for t in tasks]
        return [f.result() for f in futures]

    def task(self, x):
        print(f"Class method task {x}")
        time.sleep(0.5)
        return x + 10
example = ThreadPoolExample(max_workers=3)
results = example.run_tasks(range(5))
print("Class method ThreadPool results:", results)
        while not self.queue.empty():
            task = self.queue.get()
            print(f"Processing task: {task}")
            time.sleep(1)
            self.queue.task_done()
            time.sleep(1)
# Example of ThreadPoolExecutor in a class method
class ThreadPoolExample:
    def __init__(self, max_workers=2):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def run_tasks(self, tasks):
        futures = [self.executor.submit(self.task, t) for t in tasks]
        return [f.result() for f in futures]

    def task(self, x):
        print(f"Class method task {x}")
        time.sleep(0.5)
        return x + 10
example = ThreadPoolExample(max_workers=3)
results = example.run_tasks(range(5))