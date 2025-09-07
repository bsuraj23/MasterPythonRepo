from queue import LifoQueue

stack = LifoQueue()

stack.put('A')
stack.put('B')

print(stack.get())  # B
print(stack.get())  # A
