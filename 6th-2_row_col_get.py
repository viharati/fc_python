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

value = worksheet.acell('A1').value
print(value)

row_values = worksheet.row_values('1')
print(row_values)

col_values = worksheet.col_values('2')
print(col_values)