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
worksheet.insert_row(['insert_row:new1','insert_row:new2','insert_row:new3'],2)
	