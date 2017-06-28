#coding : utf-8
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
	'https://spreadsheets.google.com/feeds',
	'https://www.googleapis.com/auth/drive'
]

print(type(scope))

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

gc = gspread.authorize(credentials)

doc = gc.open_by_url('https://docs.google.com/spreadsheets/d/1bpAgT3ER6d-CDB4bEZj4FuPHfLPhAY1wvQiWqTxJClI/edit#gid=0')

worksheet = doc.get_worksheet(0)

values = worksheet.range('A1:C3')
print(values)


print('-'*10)
for v in values:
	print(v.value)


print('-'*10)
cur_row=1
for v in values:
	if cur_row != v.row:
		print('new row:'+str(v.row))
		cur_row=v.row

	print(v.value)


print('-'*10)
for i in range(0,2):
	for j in range(0,2):
		print(values[i*3+j].value)