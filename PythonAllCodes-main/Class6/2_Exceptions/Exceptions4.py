try:
    d = {"a": 1}
    print(d["z"])
    
    print("I amm after line 3 ")

except IndexError:
    print("Index out of range")

except KeyError:
    print("Key not found which your trying to access hfdfd ")
finally:
    print("Execution completed.I am finally block")   
