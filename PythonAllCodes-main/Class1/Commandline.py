#generate code to run this program ,to show command line argument exmaple
#command line   

import sys

if len(sys.argv) == 1:
    print("No command line arguments provided.")
else:
    print("Command line arguments:")
    for arg in sys.argv[1:]:
        print(arg)

#add more examples of command line arguments
# Example usage:
# python Commandline.py arg1 arg2 arg3
# Output:
# Command line arguments:
# arg1
# arg2
# arg3 
# ...existing code...

# More examples of command line arguments (without class)


# Example 2: Concatenate all arguments into a single string
if len(sys.argv) > 1:
    concatenated = " ".join(sys.argv[1:])
    print("Concatenated arguments:", concatenated)

# Example 3: Count the number of arguments
print("Number of command line arguments (excluding script name):", len(sys.argv) - 1)
