# The script will start execution
# from the code inside the
# if __name__ == "__main__": 
#     block only when you run the script directly
# (not when you import it as a module in another script). 

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print(x, y, z)
li = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if (i + j + k) < n:
#                 li.append([i, j, k])
for temp in range(3):
    print(li)
