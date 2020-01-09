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


iflation = web.DataReader('CPIAUCSL','fred',startDate,endDate)
iflation.rename(index=str, columns={'CPIAUCSL' : 'Value'}, inplace=True)#переименование столбца CPIAUCSL в Value

monthSD = pd.date_range(startDate,endDate,freq='MS') #оставляет только значения,которые сооствествуют началу месяца
MSFT = MSFT.reindex(monthSD)#меняет индекс на новые даты
MSFT = MSFT.dropna() #удаляет значения с NAN т.е нерабочие дни каждого первого числа месяца
print(MSFT)