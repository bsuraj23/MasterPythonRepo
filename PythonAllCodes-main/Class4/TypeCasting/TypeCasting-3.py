# Using indexes inside placeholders
print("Name: {0}, Age: {1}".format("Bob", 25))
# Output: Name: Bob, Age: 25

# Repeating indexes
print("First: {0}, Second: {1}, Again First: {0}".format("Red", "Blue"))
# Output: First: Red, Second: Blue, Again First: Red

# Named placeholders
print("Product: {name}, Price: ${price}".format(name="Pen", price=1.5))
# Output: Product: Pen, Price: $1.5

