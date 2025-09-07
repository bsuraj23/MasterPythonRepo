class Person:
    pass

p = Person()

# setattr()
setattr(p, 'name', 'Alice')
setattr(p, 'age', 30)
setattr(p, 'country', 'India')
setattr(p, 'status', True)
setattr(p, 'score', 99.5)

# getattr()
print(getattr(p, 'name'))
print(getattr(p, 'age'))
print(getattr(p, 'country'))
print(getattr(p, 'status'))
print(getattr(p, 'score'))

# delattr()
delattr(p, 'score')
# print(p.score)  # Will raise error after deletion
setattr(p, 'score', 88.0)
delattr(p, 'status')
# print(p.status)  # Will raise error after deletion
