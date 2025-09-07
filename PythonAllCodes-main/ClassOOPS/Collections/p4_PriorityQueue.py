from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, "code"))
pq.put((1, "eat"))
pq.put((3, "sleep"))

while not pq.empty():
    print(pq.get())  # (1, 'eat'), (2, 'code'), (3, 'sleep')
