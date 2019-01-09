import requests
from bs4 import BeautifulSoup
import xlsxwriter

r=requests.get("http://www.world-nuclear.org/information-library/facts-and-figures/uranium-production-figures.aspx")
soup=BeautifulSoup(r.content, "html.parser")

# Headers:
Head= soup.thead.find_all('td')
HeadData=[]

for i in Head:
    HeadData.append(i.text)
DataList=[]
table_body=soup.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    row=[x.text.strip() for x in row()]
    DataList.append(row)
FinalList=[]

for i in DataList:
    dict1={}
    for item1, item2 in zip(HeadData, i):
      dict1.update({item1:item2})
    FinalList.append(dict1)

workbook = xlsxwriter.Workbook('WorldNuclearAssociation.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

for i in HeadData:
    worksheet.write(row,col, i)
    col+=1
col=0




# 1st
row=1
for i in FinalList:
        worksheet.write(row, col, i['Country'])
        row+=1
# 2nd
row=1
col=1
for i in FinalList:
        Year1=i['2008']
        worksheet.write(row, col, Year1)
        row+=1
# 3rd
row=1
col=2

for i in FinalList:
        Year2=i['2009']
        worksheet.write(row, col, Year2)
        row+=1
# 4th
row=1
col=3

for i in FinalList:
        Year3=i['2010']
        worksheet.write(row, col, Year3)
        row+=1
# 5th
row=1
col=4

for i in FinalList:
        Year4=i['2011']
        worksheet.write(row, col, Year4)
        row+=1
# 6th
row=1
col=5

for i in FinalList:
        Year5=i['2012']
        worksheet.write(row, col, Year5)
        row+=1
# 7th
row=1
col=6

for i in FinalList:
        Year6=i['2013']
        worksheet.write(row, col, Year6)
        row+=1
#8th
row=1
col=7

for i in FinalList:
        Year7=i['2014']
        worksheet.write(row, col, Year7)
        row+=1
# 9 
row=1
col=8

for i in FinalList:
        Year8=i['2015']
        worksheet.write(row, col, Year8)
        row+=1
# 10th
row=1
col=9

for i in FinalList:
        Year9=i['2016']
        worksheet.write(row, col, Year9)
        row+=1
# 11th
row=1
col=10

for i in FinalList:
        Year10=i['2017']
        worksheet.write(row, col, Year10)
        row+=1
workbook.close()




