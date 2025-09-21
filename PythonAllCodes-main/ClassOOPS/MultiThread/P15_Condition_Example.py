
import threading
import time

condition = threading.Condition()
shared_data = []

def consumer():
    with condition:
        print("Consumer waiting for data...")
        condition.wait()
        print("Consumer received:", shared_data[0])

def producer():
    time.sleep(1)
    with condition:
        shared_data.append("important data")
        print("Producer produced data")
        condition.notify()

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)
t1.start()
t2.start()
t1.join()
t2.join()

# Additional example: Multiple consumers waiting for a single producer
def multi_consumer(id):
    with condition:
        print(f"Consumer {id} waiting for data...")
        condition.wait()
        print(f"Consumer {id} received:", shared_data[0])
consumers = [threading.Thread(target=multi_consumer, args=(i,)) for i in range(3)]
for c in consumers:
    c.start()
time.sleep(1)
with condition:
    shared_data.append("shared resource")
    print("Producer produced shared resource")
    condition.notify_all()
for c in consumers:
    c.join()
# Example of Condition in a class method
class SharedResource:
    def __init__(self):
        self.condition = threading.Condition()
        self.data = None

    def produce(self, value):
        with self.condition:
            self.data = value
            print("Produced:", value)
            self.condition.notify()

    def consume(self):
        with self.condition:
            while self.data is None:
                print("Consumer waiting for data...")
                self.condition.wait()
            print("Consumed:", self.data)
            self.data = None
resource = SharedResource()
t3 = threading.Thread(target=resource.consume)
t4 = threading.Thread(target=resource.produce, args=("some data",))