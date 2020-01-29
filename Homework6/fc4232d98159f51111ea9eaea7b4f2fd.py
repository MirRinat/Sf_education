import pandas_datareader as wb
import pandas as pd
import datetime as date

#Шаг 1(10 баллов): Удалено скачайте "Treasury Constant Maturity Rate" с сайта фред FRED
#(https://fred.stlouisfed.org/categories/115) от 02/01/2014 до 02/01/2016 для следующих кривых:
#6-Month
#1-Year
#5-Year
#10-Year

# tickers = ["DGS6MO","DGS1","DGS5","DGS10"]
tickers_DGS6MO = ["DGS6MO"]
tickers_DGS1 = ["DGS1"]
tickers_DGS5 = ["DGS5"]
tickers_DGS10 = ["DGS10"]
source = 'fred'
startDate = '2014-01-02'
endDate = '2016-01-02'
df1 = wb.DataReader(tickers_DGS6MO,source,startDate,endDate)
df2 = wb.DataReader(tickers_DGS1,source,startDate,endDate)
df3 = wb.DataReader(tickers_DGS5,source,startDate,endDate)
df4 = wb.DataReader(tickers_DGS10,source,startDate,endDate)
# print(df1)

#Шаг 2( 5 баллов ): Определите среднее и стандартную дивиацию для каждой из кривых( кривая это 6-month, 1 year, и т.д.)

stDev1 = df1.std()
avg1 = df1.mean()

stDev2 = df2.std()
avg2 = df2.mean()

stDev3 = df3.std()
avg3 = df3.mean()

stDev4 = df4.std()
avg4 = df4.mean()

# print(stDev1)
# print(avg1)

#Шаг 3( 5 баллов ): Выберете только те даты которые имеют показателе выше или ниже avg +/- 1 std

df1 = df1[(df1 > avg1 + stDev1) | (df1 < avg1 - stDev1)]
df2 = df2[(df2 > avg2 + stDev2) | (df2 < avg2 - stDev2)]
df3 = df3[(df3 > avg3 + stDev3) | (df3 < avg3 - stDev3)]
df4 = df4[(df4 > avg4 + stDev4) | (df4 < avg4 - stDev4)]

df1 = df1.dropna()
df2 = df2.dropna()
df3 = df3.dropna()
df4 = df4.dropna()
print(df1)

#Шаг 4( 10 баллов ): Создайте объединенную dataframe в которой будут только те даты, которые будут больше или меньше
# avg +/- 1 std. Hint: подумайте про joins для dataframes из Шаг 3

dfUnited1 = df1.join(df2)
dfUnited2 = dfUnited1.join(df3)
dfUnited3 = dfUnited2.join(df4)
print(dfUnited3)

#Шаг 5( 5 баллов): Сохраните сгенерированный файл как sigma.xlsx
#Загрузите этот заполенный файл и sigma.xlsx

dfUnited3.to_excel('sigma.xlsx')