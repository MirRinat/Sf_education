# coding=<utf-8>
# -*- coding: <utf-8> -*-
# vim: set fileencoding=<utf-8> :
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import wb
import quandl

#####download Microsoft's stocks#####
startDate = '2015-1-1'
endDate = dt.datetime.today()
MSFT = web.DataReader("MSFT",'yahoo',startDate,endDate)
MSFTSelected = MSFT['Close']

stDev = MSFTSelected.std() #среднее квадратичное отклонение
avg = MSFTSelected.mean() #среднее значение

print("stDev = ",stDev)
print("avg = ", avg)

#MSFTOneSigma = MSFT[MSFT['Close'] > (MSFT['Close'].mean() + 2.4 * stDev)]
#print('MSFTOneSigma = ',MSFTOneSigma)


inflation = web.DataReader('CPIAUCSL', 'fred', startDate, endDate)
inflation.rename(index=str, columns={'CPIAUCSL' : 'Value'}, inplace=True)#переименование столбца CPIAUCSL в Value

monthSD = pd.date_range(startDate,endDate,freq='MS') #оставляет только значения,которые сооствествуют началу месяца
MSFT = MSFT.reindex(monthSD)#меняет индекс на новые даты
MSFT = MSFT.fillna(method = 'ffill') #заменяет NAN на значения value,но method = ffill заменяет предыдущие значения в строках выше
#MSFT = MSFT.dropna() #удаляет значения с NAN т.е нерабочие дни каждого первого числа месяца
#print(MSFT)
inflation = inflation.assign(Prev = inflation['Value'].shift(1))#создание новой колонки

def calculateTheDiff(row):
    return row['Value']/row['Prev'] - 1

inflation['pctChange0'] = inflation.apply(lambda row:calculateTheDiff(row), axis=1)#определение процентного изменения с предыдущим показателем
inflation['pctChange1'] = inflation.apply(lambda row: (row['Value'] / row.shift(-1)['Value'] - 1), axis=1)#определение процентного изменения с предыдущим показателем методом lambda
inflation = inflation.assign(pctChange2 = inflation['Value'].pct_change())#определение процентного измененияс предыдущим показателем методом из библиотеки pandas
inflation.to_excel('recData/chngInflation.xlsx')

inflation.drop(['Prev', 'pctChange0', 'pctChange1', 'pctChange2'], axis=1, inplace=True)#удаление столбцов
inflation['currentPrice'] = inflation.apply(lambda row:inflation.tail(1)['Value']/row['Value'],axis=1)

pricesWithInflation = inflation.join(MSFT['Close'])
pricesWithInflation['priceInCurrentDollars'] = pricesWithInflation['currentPrice'] * pricesWithInflation['Close']
pricesWithInflation[['priceInCurrentDollars','Close']].plot()
plt.show()

