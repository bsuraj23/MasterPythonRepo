import threading
import time

def func():
    for temp in range(10):
        print(f"[{threading.current_thread().name}] Thread is running!")
        time.sleep(1)

# Define a function to run in a thread
def print_numbers():
    for i in range(15):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(1)

# Create multiple threads
thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=func, name="Thread-2")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Main thread: All threads finished.")
if __name__ == "__main__":
    # This guard is essential for multithreading  on Windows
    demonstrate_multithreading()