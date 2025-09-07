# Keyword Arguments - 6 Examples

# Example 1
def user_info(name, age):
    print(name, age)

user_info(age=30, name="Bob")

# Example 2
def area(length, breadth):
    return length * breadth

print(area(breadth=8, length=4))

# Example 3
def discount(price, percentage):
    return price * percentage / 100

print(discount(percentage=5, price=300))

# Example 4
def rectangle_perimeter(length, width):
    return 2 * (length + width)

print(rectangle_perimeter(width=5, length=12))

# Example 5
def tax(price, rate=0.05):
    return price * rate

print(tax(rate=0.1, price=2000))

# Example 6
def full_name(first, last):
    print(first, last)

full_name(last="Smith", first="Anna")
