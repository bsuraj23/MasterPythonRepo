#accessign global variable inside function using global function
# # global Keyword
a=10        
def f1():
    a=777
    print("value of a inside f1",a) 
    print(globals())   #gives all global variables in dict format
    print("globals a is ",globals()['a'])  #accessing global variable using globals() function
f1()
print("value of a outside f1",a)    

#TODO
#add more complex examples
#add example of nested function and accessing global variable inside nested function    
