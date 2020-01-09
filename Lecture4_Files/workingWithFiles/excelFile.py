import openpyxl as xl

file = xl.load_workbook('Sample.xlsx')
sheet = file.active
#print(sheet['A'][2].value)

#сосчтитать выручку по регионам за 2016 год
region16Revenue = {}

for row in sheet.iter_rows(min_row=2):
    if row[0].value:
        region = row[0].value
        rev16 = row[3].value
        region16Revenue[region] = region16Revenue.get(region,0) + rev16

print(region16Revenue)

