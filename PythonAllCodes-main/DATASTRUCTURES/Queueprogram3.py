from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def is_empty(self):
        return not self.items
    
# Demo usage
if __name__ == "__main__":
    q = Queue()
    print("Queue empty?", q.is_empty())
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueues:", list(q.items))
    print("Dequeued:", q.dequeue())
    print("Queue now:", list(q.items))
    print("Queue empty?", q.is_empty())