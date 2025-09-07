a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# intersection method  
# #example 1      
# print(a.intersection(b))

# Exampless on differeences 
print("before a df update ",a)
result = b.difference(a) 

#add example for difference update and update


# b.difference_update(a)
print("After a df  ",result)
# print("After a df update ",a)


a = {1, 2, 3}
b = {2, 3, 4}

union = a | b
result = a.union(b)
print("union ",union)
print("union ",result)

print("line 25",set('abc') & set('bcd'))
print({5, 6} & {6, 7})
print(set([1, 2, 3]) & set([3, 4]))

# more exampls for only difference and difference update 
# intersection symbol or keyword 
print(a)
# a.copy(b)
print(a)
print("line 38",a.difference(b))
print("line 39",a.intersection(b))
print("line 40",a)
print("line 41",b)
result = a.difference_update(b)
print("line 40",result)




