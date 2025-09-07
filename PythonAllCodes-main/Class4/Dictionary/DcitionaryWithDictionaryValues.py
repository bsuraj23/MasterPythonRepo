d = {'emp1': {'name': 'John', 'age': 30}}
d2 = {'a': {'x': 1}, 'b': {'y': 2}}
d3 = {'nested': {'key': 'value'}}
d4 = {'person': {'name': 'Alice', 'id': 101}}
d5 = {'outer': {'inner': {'leaf': 'node'}}}
print(d)
print(d2)
print(d3)
print(d4)
print(d5)

# add example for iterations of dict
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")    
for key, value in d2.items():
    print(f"Key: {key}, Value: {value}")

# Iterating over nested dictionary values
for key, value in d.items():
    for inner_key, inner_value in value.items():
        print(f"{key} -> {inner_key}: {inner_value}")

# Iterating and printing all keys and values in d5 (deeply nested)
def print_nested_dict(dct, parent_key=""):
    for k, v in dct.items():
        if isinstance(v, dict):
            print_nested_dict(v, f"{parent_key}{k}.")
        else:
            print(f"{parent_key}{k}: {v}")

print("Deeply nested dictionary d5:")
print_nested_dict(d5)

# Collecting all values from d2 into a list
all_values = []
for value in d2.values():
    all_values.extend(value.values())
print("All values in d2:", all_values)

# Using dictionary comprehension to flatten d3
flat_d3 = {f"{outer_key}_{inner_key}": inner_value for outer_key, inner_dict in d3.items() for inner_key, inner_value in inner_dict.items()}
print("Flattened d3:", flat_d3)

# Checking if a key exists in a nested dictionary (d4)
key_to_check = "id"
if key_to_check in d4["person"]:
    print(f"Key '{key_to_check}' found in d4['person']: {d4['person'][key_to_check]}")
else:
    print(f"Key '{key_to_check})'