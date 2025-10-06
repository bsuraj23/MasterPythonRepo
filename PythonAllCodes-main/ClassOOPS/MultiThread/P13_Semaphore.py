#Add theory below

"""
Semaphore is a synchronization primitive that is used to control access to a shared resource by multiple threads. It maintains a count that represents the number of permits available for threads to acquire. When a thread wants to access the shared resource, it must acquire a permit from the semaphore. If no permits are available, the thread will block until a permit is released by another thread.
"""




#TODO callable runnable  compare with Java and how its in python 

#code below
 
 



import threading
import time

sema = threading.Semaphore(2)

def semaphore_example(i):
    with sema:
        print(f"Thread {i} entered semaphore")
        time.sleep(1)
        print(f"Thread {i} leaving semaphore")

threads = [threading.Thread(target=semaphore_example, args=(i,)) for i in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# Additional example: Semaphore in a producer-consumer scenario
buffer = []
buffer_size = 3
produced_items = 0
consumed_items = 0
empty_slots = threading.Semaphore(buffer_size)
full_slots = threading.Semaphore(0)
buffer_lock = threading.Lock()
def producer():
    global produced_items
    for _ in range(5):
        item = produced_items
        empty_slots.acquire()
        with buffer_lock:
            buffer.append(item)
            print(f"Produced: {item}")
            produced_items += 1
        full_slots.release()
        time.sleep(0.5)

def consumer():
    global consumed_items
    for _ in range(5):
        full_slots.acquire()
        with buffer_lock:
            item = buffer.pop(0)
            print(f"Consumed: {item}")
            consumed_items += 1
        empty_slots.release()
        time.sleep(0.5)
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start() 
producer_thread.join()
consumer_thread.join()  