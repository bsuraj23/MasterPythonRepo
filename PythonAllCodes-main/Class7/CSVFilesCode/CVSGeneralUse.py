# Example 1: Read CSV file
import csv
with open('sample.csv', 'r') as f:
    for row in csv.reader(f):
        print(row)

# Example 2: Write CSV file
with open('sample.csv', 'w', newline='') as f:
    csv.writer(f).writerow(['A', 'B', 'C'])

# Example 3: DictReader
with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Example 4: DictWriter
with open('dict_sample.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Age'])
    writer.writeheader()
    writer.writerow({'Name': 'John', 'Age': 25})

# Example 5: CSV Handling Exception
try:
    with open('sample.csv') as f:
        reader = csv.reader(f)
except FileNotFoundError:
    print("CSV file not found.")
