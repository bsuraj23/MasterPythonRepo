
import threading
import time
from queue import Queue

q = Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")
        time.sleep(0.5)

def consumer():
    for _ in range(5):
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()

# Additional example: Multiple producers and consumers
def multi_producer(id):
    for i in range(3):
        item = f"P{id}-{i}"
        q.put(item)
        print(f"Producer {id} produced {item}")
        time.sleep(0.5)
def multi_consumer(id):
    for _ in range(3):
        item = q.get()
        print(f"Consumer {id} consumed {item}")
        q.task_done()
        time.sleep(1)
producers = [threading.Thread(target=multi_producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=multi_consumer, args=(i,)) for i in range(2)]
for p in producers:
    p.start()   
for c in consumers:
    c.start()
for p in producers:
    p.join()
for c in consumers:
    c.join()
q.join()
# Example of Queue in a class method
class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        self.queue.put(task)
        print(f"Task added: {task}")

    def process_tasks(self):
        while not self.queue.empty():
            task = self.queue.get()
            print(f"Processing task: {task}")
            time.sleep(1)
            self.queue.task_done()
task_queue = TaskQueue()
task_queue.add_task("Task1")
task_queue.add_task("Task2")
task_queue.process_tasks()
task_queue.queue.join()

# Final join to ensure all tasks are completed
q.join()
# Final join to ensure all tasks are completed
q.join()
# Final join to ensure all tasks are completed
task_queue.queue.join() 
task_queue.queue.join()
