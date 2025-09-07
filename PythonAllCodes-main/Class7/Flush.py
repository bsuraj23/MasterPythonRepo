# Example 1
f = open("flush.txt", "w")
f.write("Data before flush")
f.flush()

# Example 2
f.write("\nMore data")
f.flush()

# Example 3
import sys
sys.stdout.write("Hello")
sys.stdout.flush()

# Example 4
f.write("Flushing after writing\n")
f.flush()

# Example 5
f.close()
