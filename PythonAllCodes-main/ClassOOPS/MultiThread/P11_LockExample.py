
import threading  shared_counter = 0 lock = threading.Lock() 
 def increment_with_lock():   
      global shared_counter   
   for _ in range(10000):       
      with lock:            
         shared_counter += 1  threads = [threading.Thread(target=increment_with_lock) for _ in range(5)] for t in threads:     t.start() for t in threads:     t.join()  print("Final counter value with lock:", shared_counter)
threads = [threading.Thread(target=increment_with_lock) for _ in range(5)]
for t in threads:     t.start()
for t in threads:     t.join()
print("Final counter value with lock:", shared_counter)
shared_counter = 0

lock = threading.Lock()
def increment_with_lock():
    global shared_counter
    for _ in range(10000):
        with lock:
            shared_counter += 1
threads = [threading.Thread(target=increment_with_lock) for _ in range(5)]
for t in threads:     t.start()
for t in threads:     t.join()
print("Final counter value with lock:", shared_counter)