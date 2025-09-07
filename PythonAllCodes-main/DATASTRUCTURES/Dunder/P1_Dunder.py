class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages


# Testing the Book class
book1 = Book("Harry Potter", 350)
book2 = Book(" Jackson", 350)

print(book1)               # Book: Harry Potter, Pages: 350  --> Uses __str__
print(len(book1))          # 350  --> Uses __len__
print(book1 == book2)      # True  --> Uses __eq__
