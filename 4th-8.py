from openpyxl import load_workbook

wb=load_workbook('my_result.xlsx')
data = wb['Sheet']

t_data = data['A2:B5']
print(t_data[0][0].value)
print(t_data[1][0].value)
print(t_data[0][1].value)

print('-*'*10)

for row in t_data:
	for cell in row:
		print(cell.value)