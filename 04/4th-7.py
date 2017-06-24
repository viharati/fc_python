from openpyxl import load_workbook
wb = load_workbook('my_result.xlsx')
print(wb.get_sheet_names())
data= wb.active
data=wb['sheet_test']
data=wb['Sheet']

rows = data[2]
for col in rows:
	print(col.value)


print('-'*10)
cols = data['B']
for row in cols:
	print(row.value)