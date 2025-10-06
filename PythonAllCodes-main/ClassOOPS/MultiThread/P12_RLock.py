
import threading

rlock = threading.RLock()

def rlock_example():
    with rlock:
        print("RLock acquired first time")
        with rlock:
            print("RLock acquired second time (reentrant)")

threading.Thread(target=rlock_example).start()

threading.Thread(target=rlock_example).start()
rlock.release()

#Add more examples
# Example of RLock in a recursive function
def recursive_function(n):
    with rlock:
        if n > 0:
            print(f"Recursion level: {n}")
            recursive_function(n - 1)   
        else:
            print("Base case reached")
recursive_function(3)
# Example of RLock in a class method
class Counter:
    def __init__(self):
        self.value = 0
        self.rlock = threading.RLock()

    def increment(self):
        with self.rlock:
            self.value += 1
            print(f"Counter value: {self.value}")
counter = Counter()
threads = [threading.Thread(target=counter.increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()    
print(f"Final counter value: {counter.value}")
