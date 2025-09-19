from queue import Queue
q2 = Queue()
q = Queue()

# Add elements
q.put(10)
q.put(20)

# Remove elements
print(q.get())  # 10
print(q.get())  # 20

print(dir(q))
print(q.queue)
print(q.empty())
print(q.full())
print(q.qsize())    





