dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];



SN	Function with Description
1	cmp(dict1, dict2)
Compares elements of both dict.
2	len(dict)
Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
3	str(dict)
Produces a printable string representation of a dictionary
4	type(variable)
Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.
Python includes following dictionary methods

SN	Methods with Description
1	dict.clear()
Removes all elements of dictionary dict
2	dict.copy()
Returns a shallow copy of dictionary dict
3	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.
4	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary
5	dict.has_key(key)
Returns true if key in dictionary dict, false otherwise
6	dict.items()
Returns a list of dict's (key, value) tuple pairs
7	dict.keys()
Returns list of dictionary dict's keys
8	dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict
9	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict
10	dict.values()
Returns list of dictionary dict's values
