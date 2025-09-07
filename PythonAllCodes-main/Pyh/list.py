list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];



print(list1)
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

#we can change list content // list1[3]=1998 will make above on 1997 1998

# len, min, max,list(seq)// converts a tuple to list


SN	Methods with Description
1	list.append(obj)
Appends object obj to list
2	list.count(obj)
Returns count of how many times obj occurs in list
3	list.extend(seq)
Appends the contents of seq to list
4	list.index(obj)
Returns the lowest index in list that obj appears
5	list.insert(index, obj)
Inserts object obj into list at offset index
6	list.pop(obj=list[-1])
Removes and returns last object or obj from list
7	list.remove(obj)
Removes object obj from list
8	list.reverse()
Reverses objects of list in place
9	list.sort([func])
Sorts objects of list, use compare func if given
