import multiprocessing
import time

def square_numbers():
    for i in range(3):
        print(f"[{multiprocessing.current_process().name}] Square of {i} is {i*i}")
        time.sleep(1)

# Create processes
p1 = multiprocessing.Process(target=square_numbers, name="Process-1")
p2 = multiprocessing.Process(target=square_numbers, name="Process-2")

# Start and join
p1.start()
p2.start()

p1.join()
p2.join()

print("Main process: All subprocesses completed.")
