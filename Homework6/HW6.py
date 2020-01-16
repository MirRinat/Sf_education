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

dfSixMonth = wb.DataReader(tickers[0],'fred',start,end)
dfOneYear = wb.DataReader(tickers[1],'fred',start,end)
dfFiveYear = wb.DataReader(tickers[2],'fred',start,end)
dfTenYear = wb.DataReader(tickers[3],'fred',start,end)


# dgsDict = {}
# for tic in tickers:
#     dgsDict[tic] = wb.DataReader(tic,'fred',start,end)
#     dgsDict[tic] = dgsDict[tic].dropna()
# print(dgsDict)
#dict["DGS6MO"] = wb.DataReader("DGS6MO",'fred',start,end)
#Шаг 2( 5 баллов ): Определите среднее и стандартную дивиацию для каждой из кривых( кривая это 6-month, 1 year, и т.д.)
# stdDev = dgs.std()
# avg = dgs.mean()
# print("Среднее отклонение\n",stdDev)
# print("Стандартное отклонение\n", avg)
# stdDict = {}
# avgDict = {}
# for tic in tickers:
#     stdDict[tic] = dgsDict[tic].std()
#     avgDict[tic] = dgsDict[tic].mean()
# print(stdDict)

dfSixMonthStd = dfSixMonth.std()
dfOneYearStd = dfOneYear.std()
dfFiveYearStd = dfFiveYear.std()
dfTenYearStd = dfTenYear.std()

dfSixMonthMean = dfSixMonth.mean()
dfOneYearMean = dfOneYear.mean()
dfFiveYearMean = dfFiveYear.mean()
dfTenYearMean = dfTenYear.mean()

#Шаг 3( 5 баллов ): Выберете только те даты которые имеют показателе выше или ниже avg +/- 1 std

dfSixMonth = dfSixMonth[dfSixMonth > (dfSixMonthStd + dfSixMonthMean) |
                        dfSixMonth < (dfSixMonthStd - dfSixMonthMean)]
dfOneYear = dfOneYear[dfOneYear > (dfOneYearStd + dfOneYearMean) |
                        dfOneYear < (dfOneYearStd - dfOneYearMean)]
dfFiveYear = dfFiveYear[dfFiveYear > (dfFiveYearStd + dfFiveYearMean) |
                        dfFiveYear < (dfFiveYearStd - dfFiveYearMean)]
dfTenYear = dfTenYear[dfTenYear > (dfTenYearStd + dfTenYearMean) |
                        dfTenYear < (dfTenYearStd - dfTenYearMean)]


#Шаг 4( 10 баллов ): Создайте объединенную dataframe в которой будут только те даты, которые будут больше или меньше
# avg +/- 1 std. Hint: подумайте про joins для dataframes из Шаг 3

dfUnited =




# for tic in tickers:
#     dgs[tic] = dgsDict[[(dgsDict[tic]) > (avgDict[tic] + stdDict[tic]) | (dgsDict[tic] < (avgDict[tic] - stdDict[tic]))]]
#     # print(dgsSigmaDict[tic])

# dgsSixMonth = dgs[(dgs['DGS6MO'] > (avgDict['DGS6MO'] + stdDict['DGS6MO'])) |
#                   (dgs['DGS6MO'] < (avgDict['DGS6MO'] -  stdDict['DGS6MO']))]
# dgsOneYear = dgs[(dgs["DGS1"] > (avgDict["DGS1"] + stdDict["DGS1"])) |
#                   (dgs["DGS1"] < (avgDict["DGS1"] - stdDict["DGS1"]))]
# dgsFiveYear = dgs[(dgs["DGS5"] > (avgDict["DGS5"] + stdDict["DGS5"])) |
#                   (dgs["DGS5"] < (avgDict["DGS5"] -  stdDict["DGS5"]))]
# dgsTenYear = dgs[(dgs["DGS10"] > (avgDict["DGS10"] + stdDict["DGS10"])) |
#                   (dgs["DGS10"] < (avgDict["DGS10"] -  stdDict["DGS10"]))]

#Шаг 5( 5 баллов): Сохраните сгенерированный файл как sigma.xlsx
#Загрузите этот заполенный файл и sigma.xlsx
# dgsOneSigma.to_excel('sigma.xlsx')
