#coding:utf-8
from openpyxl import load_workbook

wb = load_workbook('textfile.xlsx')
sheet = wb['Sheet1']

print(sheet['B1'].value)

sheet['B1']='asdf'

print(sheet['B1'].value)
