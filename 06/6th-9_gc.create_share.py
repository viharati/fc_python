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

gsheet = gc.create('테스트문서-ver3+2')

#gsheet.share('viharaty@gmail.com','user','reader/writer')
gsheet.share('viharaty@gmail.com','user','owner')
gsheet.share('woncocoa@gmail.com','user','writer')

worksheet = gsheet.add_worksheet('추가시트1', '1', '1')

for i in range(10):
    worksheet.insert_row([str(i)+'Data'],1)