from openpyxl import Workbook
nfc_east = ('DAL', 'WAS', 'PHI', 'NYG')
wb = Workbook()
ws = wb.active
for row, i in enumerate(nfc_east):
    column_cell = 'A'
    ws[column_cell+str(row+2)] = str(i)

# Save the file
wb.save("sample.xlsx")

# a = [1, 5, 3, 2, 6]
# d = a.count(1)
# print d