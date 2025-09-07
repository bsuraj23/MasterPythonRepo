def f():
    global s
    print (s)
    s = "That's clear."
    print (s) 


s = "Python is great!" 
f()
print (s)
