import multiprocessing

def add():
    print("Process started!")

process = multiprocessing.Process(target=add)
print(process)
process.start()  # Starts running the task in a separate process
process.kill()
