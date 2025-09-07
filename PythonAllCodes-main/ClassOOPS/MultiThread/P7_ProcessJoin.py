import multiprocessing
import time

def task():
    print("Process working...")
    time.sleep(2)
    print("Process finished!")

process = multiprocessing.Process(target=task)
process.start()

process.join()
print("Main program waited for process to finish.")
process.kill()