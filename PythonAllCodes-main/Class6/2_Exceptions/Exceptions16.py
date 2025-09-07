try:
    open("file.txt")
except FileNotFoundError:
    print("FileNotFoundError occurred")
