from openpyxl import load_workbook


file = 'db_1.xlsx'
wb1 = load_workbook(filename=file)
sheet_ranges = wb1['price']

sheet_ranges['y1'].value = '123'
sheet_ranges.append([1, 2, 4])

print(sheet_ranges['a1'])

wb1.save(file)
