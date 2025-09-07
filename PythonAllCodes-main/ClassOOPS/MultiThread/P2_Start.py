import threading

def task():
    print("Thread has started!")

# Create and start the thread
my_thread = threading.Thread(target=task)
  # Starts running in parallel
my_thread.start()
