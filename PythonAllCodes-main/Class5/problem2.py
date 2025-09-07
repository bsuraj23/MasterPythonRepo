if __name__ == "__main__":
    n = int(input())
    newList = list(map(int, input().split()))

max_value = -5000


for temp in newList:
    print("temp is ", temp)
    print("newList is ", newList)
    if temp > max_value:
        max_value = temp
print("Answer is ", max_value)
