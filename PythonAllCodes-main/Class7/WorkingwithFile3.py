# Example 1: Copy data from one file to another
with open("source.txt", "r") as src, open("target.txt", "w") as tgt:
    tgt.write(src.read())

# Example 2: Line by line migration
with open("source.txt", "r") as src, open("target2.txt", "w") as tgt:
    for line in src:
        tgt.write(line)

# Example 3: Reading lines and appending
lines = open("source.txt").readlines()
with open("target3.txt", "a") as tgt:
    tgt.writelines(lines)

# Example 4: Uppercasing during migration
with open("source.txt", "r") as src, open("target4.txt", "w") as tgt:
    tgt.write(src.read().upper())

# Example 5: Migrating selective data
with open("source.txt", "r") as src, open("target5.txt", "w") as tgt:
    for line in src:
        if "Python" in line:
            tgt.write(line)
