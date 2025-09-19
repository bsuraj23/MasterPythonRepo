import threading

def task():
  for temp in range(5):
        print("Thread is running! from other parallel thread")




# Create and start the thread
my_thread = threading.Thread(target=task)
  # Starts running in parallel


def task():
   for temp in range(5):
        print("Thread is running! from main thread")
task()
