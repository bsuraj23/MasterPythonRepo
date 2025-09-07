
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return not self.items

# Demo usage
if __name__ == "__main__":
    s = Stack()
    print("Stack empty?", s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack after pushes:", s.items)
    print("Top element (peek):", s.peek())
    print("Popped:", s.pop())
    print("Stack now:", s.items)
    print("Stack empty?", s.is_empty())