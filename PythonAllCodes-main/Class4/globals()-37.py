def F():
    global x
    x = 1

def G():
    print(globals()["x"]) #will return value of global 'x', which is 1
    x=90

    a=locals()
    print(a)

def H():
    print(x) #will also return value of global 'x', which, also, is 1

F()
G()
H()
