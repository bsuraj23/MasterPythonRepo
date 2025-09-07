from queue import Queue
q2 = Queue()
q = Queue()

# Add elements
q.put(10)
q.put(20)

# Remove elements
print(q.get())  # 10
print(q.get())  # 20


