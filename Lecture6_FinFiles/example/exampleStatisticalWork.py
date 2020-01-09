import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import wb
import quandl

#Загрузить акции Майкрософт
startDate = '2013-1-1'
endDate = dt.datetime.today()

MSFT = web.DataReader('MSFT','google',startDate, endDate)
MSFTSelected = MSFT['Close']
#print(MSFTSelected)

stDev = MSFT['Close'].std()
avg = MSFT['Close'].mean()

inflation = web.DataReader('CPIAUCSL','fred',startDate,endDate)
inflation.rename(index=str, columns={'CPIAUCSL' : 'Value'}, inplace=True)

inflation = inflation.assign( Prev = inflation['Value'].shift(1) )


def calculateTheDiff(row):
    return row['Value']/row['Prev'] - 1

inflation['pctChange0'] = inflation.apply(lambda row: calculateTheDiff(row), axis=1)



inflation['pctChange1'] = inflation.apply(lambda row: (row['Value']/row['Prev'] - 1), axis=1)


#=B3/B2-1
inflation['pctChange2'] = inflation.apply(lambda row: (row['Value']/row.shift(-1)['Value'] -1), axis=1)



inflation = inflation.assign( pctChange3 = inflation['Value'].pct_change())

#=$B$62/B3
inflation['currentPrice'] = inflation.apply(lambda row: (inflation.tail(1)['Value'] / row['Value']), axis = 1)
inflation.drop(['Prev', 'pctChange0', 'pctChange1', 'pctChange2', 'pctChange3'],axis=1,inplace = True)

pricesWInflation = inflation.join(MSFT['Close'])
pricesWInflation['priceInCurrentDollars'] = pricesWInflation['currentPrice'] * pricesWInflation['Close']

pricesWInflation[['priceInCurrentDollars','Close']].plot()
plt.show()