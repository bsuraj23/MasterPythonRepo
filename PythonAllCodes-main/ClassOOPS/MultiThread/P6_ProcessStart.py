import multiprocessing

def add():
    print("Process started!")

process = multiprocessing.Process(target=add)
print(process)
process.start()  # Starts running the task in a separate process
process.kill()



#shall wekill it mandatory or not 

#code to make process connect to other new thread
#code for hello world in new process
def hello_world():
    print("Hello, World!")

process = multiprocessing.Process(target=hello_world,name ="Process-1")
process.start()
process.join()


#TODO now make a thread and connect it to a process
