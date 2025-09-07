# Example 1: write()
with open("output.txt", "w") as f:
    f.write("Hello Python\n")

# Example 2: writelines()
lines = ["Line1\n", "Line2\n", "Line3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Example 3: write() multiple
f = open("data.txt", "w")
f.write("First line\n")
f.write("Second line\n")
f.close()

# Example 4: writelines() from list
with open("names.txt", "w") as f:
    f.writelines(["Alice\n", "Bob\n"])

# Example 5: Overwriting file
with open("overwrite.txt", "w") as f:
    f.write("Overwritten content")
