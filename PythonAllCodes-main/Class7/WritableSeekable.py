# Example 1
f = open("check.txt", "w")
print(f.writable())

# Example 2
print(f.readable())

# Example 3
print(f.seekable())

# Example 4
f = open("check_read.txt", "r")
print(f.readable())

# Example 5
f = open("check_all.txt", "w+")
print(f.readable(), f.writable(), f.seekable())
f.close()
