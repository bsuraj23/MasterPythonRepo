import multiprocessing

def task():
    print("This is a separate process!")

# Create a process
process = multiprocessing.Process(target=task)

print("Process created:", process)
