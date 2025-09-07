# Example 1: Basic CSV read
import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Example 2: Reading with delimiter
with open('data.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)

# Example 3: Reading specific columns
with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])  # print first column

# Example 4: Reading skipping header
with open('data.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# Example 5: Reading CSV as list
with open('data.csv') as file:
    data = list(csv.reader(file))
print(data)
