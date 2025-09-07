from queue import LifoQueue

stack = LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.qsize())
