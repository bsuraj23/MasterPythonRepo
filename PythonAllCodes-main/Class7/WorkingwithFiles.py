# Example 1
open("a.txt", "w").close()

# Example 2
with open("b.txt", "x") as f:
    f.write("Created with exclusive mode")

# Example 3
f = open("c.txt", "w")
f.write("Python File Handling")
f.close()

# Example 4
file = open("d.txt", "w")
file.write("Demo File")
file.close()

# Example 5
with open("e.txt", "w") as f:
    pass  # Creates empty file
