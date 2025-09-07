# Example 1: read()
with open("file.txt", "r") as f:
    print(f.read())

# Example 2: readline()
with open("file.txt", "r") as f:
    print(f.readline())

# Example 3: readlines()
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Example 4: read() with size
with open("file.txt", "r") as f:
    print(f.read(5))

# Example 5: reading using for loop
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
