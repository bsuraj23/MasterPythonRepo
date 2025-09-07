# Example 1: Open Excel file with openpyxl
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')

# Example 2: Access sheet
sheet = wb.active
print(sheet.title)

# Example 3: Read cell value
print(sheet['A1'].value)

# Example 4: Write cell value
sheet['A1'] = 'Hello Excel'
wb.save('example.xlsx')

# Example 5: Loop through rows
for row in sheet.iter_rows(values_only=True):
    print(row)
