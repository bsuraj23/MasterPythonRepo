# # # global Keyword
# sunil=10 
# def f1():
#     a=90
#     print("value of a inside f1",a)
#     print(a)
# f1()
# # print("value of f outside f1",f)

# #code to demo global keyword 
# sunil=10 
# def f1():
     
#     sunil=15
#     print("value of sunil inside f1",sunil)
# f1()
# print("value of sunil outside f1",sunil)



a = 50
def change():
    global a
    a = 10
    print("value of a inside change",a)
   
print("before calling ",a)  #before calling  50
change() # value of a inside change 50
print("After callig change ",a)  #10
# print("calling change",change())


# x = 5
# print("before calling change",x)
# def change():
#     global x
#     x = 10
#     print("value of x inside change",x)
#     return x
# change()
# print(x)







def sample():
    
    
    def add():
        print("nnested function")
        cinner= 45
        
    print("i am inside function")
    loc= 89
    print(loc)  #local
    print(var)    #glovb
    # print(cinner) 
    
var = 90  
print(var) 
 
    