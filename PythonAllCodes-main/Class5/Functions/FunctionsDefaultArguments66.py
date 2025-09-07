# Default Arguments - 6 Examples

# Example 1
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Alice")

# Example 2
def power(base, exponent=2):
    return base ** exponent

print(power(4))
print(power(4, 3))

# Example 3
def message(msg="No Message"):
    print(msg)

message()

# Example 4
def sum_numbers(a=10, b=20):
    return a + b

print(sum_numbers())

# Example 5
def repeat(word="Hello", times=3):
    for _ in range(times):
        print(word)

repeat()

# Example 6
def tax(price, rate=0.05):
    return price * rate

print(tax(1000))
