from openpyxl import load_workbook
wb=load_workbook('my_result.xlsx')
ws=wb.active

ws.append(['Number','Data'])

for i in range(10):
	ws.append([i,str(i).zfill(2)+'DataAA'])

wb.save('my_result.xlsx')