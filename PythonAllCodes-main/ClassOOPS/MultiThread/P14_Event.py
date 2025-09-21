
import threading
import time

event = threading.Event()

def event_waiter():
    print("Waiting for event to be set...")
    event.wait()
    print("Event is set! Proceeding...")

def event_setter():
    time.sleep(2)
    print("Setting event now.")
    event.set()

t1 = threading.Thread(target=event_waiter)
t2 = threading.Thread(target=event_setter)
t1.start()
t2.start()
t1.join()
t2.join()

# Additional example: Using Event to synchronize multiple threads
def worker(n):
    print(f"Worker {n} waiting for event")
    event.wait()
    print(f"Worker {n} proceeding after event is set")
threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
time.sleep(1)
print("Main thread setting event")
event.set()
for t in threads:
    t.join()
# Resetting event for demonstration
event.clear()
# Example of Event in a class method
class Task:
    def __init__(self):
        self.event = threading.Event()

    def wait_for_event(self):
        print("Task waiting for event")
        self.event.wait()
        print("Task proceeding after event is set")

    def set_event(self):
        time.sleep(1)
        print("Task setting event")
        self.event.set()    
task = Task()
t3 = threading.Thread(target=task.wait_for_event)
t4 = threading.Thread(target=task.set_event)    
t3.start()
t4.start()  
t3.join()
t4.join()
