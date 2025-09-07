import threading

# Define the task (function) for the thread
def task():
    print("Thread is running!")
def add():
    c=90+90
    print(c)

# Create the thread
my_thread = threading.Thread(target=task)

# Thread is created but not yet started
print("Thread created:", my_thread)