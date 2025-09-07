# Example 1: Basic CSV write
import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])

# Example 2: Writing multiple rows
with open('output.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([['Alice', 30], ['Bob', 25]])

# Example 3: Adding delimiter
with open('output_delim.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Product', 'Price'])

# Example 4: Writing from list
rows = [['ID', 'Value'], [1, 100], [2, 200]]
with open('data.csv', 'w', newline='') as file:
    csv.writer(file).writerows(rows)

# Example 5: Append to existing CSV
with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['End', 'Record'])
