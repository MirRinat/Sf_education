import pandas_datareader as wb
import datetime as date

#Шаг 1(10 баллов): Удалено скачайте "Treasury Constant Maturity Rate" с сайта фред FRED
#(https://fred.stlouisfed.org/categories/115) от 02/01/2014 до 02/01/2016 для следующих кривых:
#6-Month
#1-Year
#5-Year
#10-Year
start = '2014-01-02'
end = '2016-01-02'
tickers = ["DGS6MO","DGS1","DGS5","DGS10"] #тут можно убрать DGS10,и результирующий dataframe не будет пуст
dgs = wb.DataReader(tickers,'fred',start,end)
dgs = dgs.dropna()
#Шаг 2( 5 баллов ): Определите среднее и стандартную дивиацию для каждой из кривых( кривая это 6-month, 1 year, и т.д.)
stdDev = dgs.std()
avg = dgs.mean()
print("Среднее отклонение\n",stdDev)
print("Стандартное отклонение\n", avg)
# for tic in tickers:
#     stdDict = {tic: dgs[tic].std()}
#     avgDict = {tic: dgs[tic].mean()}
#     print("Стандартное отклонение",tic, stdDict[tic])
#     print("Среднее отклонение",tic, avgDict[tic])

#Шаг 3( 5 баллов ): Выберете только те даты которые имеют показателе выше или ниже avg +/- 1 std
dgsOneSigma = dgs[(dgs > (avg + stdDev)) | (dgs < (avg - stdDev))]
dgsOneSigma.dropna(inplace=True)
print(dgsOneSigma)

#Шаг 5( 5 баллов): Сохраните сгенерированный файл как sigma.xlsx
#Загрузите этот заполенный файл и sigma.xlsx
dgsOneSigma.to_excel('sigma.xlsx')
