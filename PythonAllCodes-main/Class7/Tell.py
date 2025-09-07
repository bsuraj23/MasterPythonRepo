# Example 1
f = open("tell.txt", "w+")
f.write("12345")
print(f.tell())

# Example 2
f.write("67890")
print(f.tell())

# Example 3
f.seek(0)
print(f.tell())

# Example 4
f.read(2)
print(f.tell())

# Example 5
f.close()
