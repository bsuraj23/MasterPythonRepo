# Example 1
f = open("seek.txt", "w+")
f.write("Hello Seek!")
f.seek(0)
print(f.read())

# Example 2
f.seek(6)
f.write("World")
f.seek(0)
print(f.read())

# Example 3
f = open("seek_demo.txt", "w+")
f.write("abcdefghij")
f.seek(5)
print(f.read())

# Example 4
f.seek(0, 0)
print(f.read(3))

# Example 5
f.seek(0)
f.close()
