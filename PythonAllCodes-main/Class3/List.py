# print("List is same as List in Java")
# print("Insertion order is preserved")
# print("Hetrogenious Object can be aded")
# print("Duplicates can be added")
# print("Growable in Nature")
# print("Values shall be enclosed with sqaure brackets")
sampth  = list(range(1,11))
print("sampth is ",sampth)


list= ["1", "2", 23, 45.45454,23]
print(list)
print(list[0])
print(list[-2])
print("Before over riding ",list)
list[1] = 99909999
print("After over riding ",list)
list[0] = 99
print("After 2 nd time over riding ",list)
#[99, 99909999, 23, 45.45454, 23]
print(list)
list.append("Bhanu")
print("After append function",list)
list = list * 2
print("printing List after * 2", list)
list.append("Mohan")

# print("Before list[4]  action  ",list)
# list[4] = "mohan"
# print("\n\n\n\n")
# print("After Replacing   and chnagig suraj ",list)
# # a = 90
# # print(a)
# # a = 12
# # print(a)
