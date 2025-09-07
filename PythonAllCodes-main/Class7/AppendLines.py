# Example 1
with open("append.txt", "a") as f:
    f.write("Appended line 1\n")

# Example 2
with open("append.txt", "a") as f:
    f.write("Appended line 2\n")

# Example 3
with open("append_log.txt", "a") as f:
    f.write("New log entry\n")

# Example 4
with open("append_numbers.txt", "a") as f:
    f.write("12345\n")

# Example 5
with open("append_list.txt", "a") as f:
    f.writelines(["Line A\n", "Line B\n"])
