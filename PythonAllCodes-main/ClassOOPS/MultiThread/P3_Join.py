import threading
import time

def task():
    print("Thread started working...")
    time.sleep(2)
    print("Thread finished!")

# Create and start the thread
my_thread = threading.Thread(target=task)
my_thread.start()

# Wait until the thread is done
my_thread.join()
print("Main program waited until thread finished.")
