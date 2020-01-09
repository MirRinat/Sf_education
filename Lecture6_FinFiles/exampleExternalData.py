import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import wb
import quandl

###GETTING DATA######
magnit = pd.read_csv('data/MGNT_59331.csv')
magnit.set_index('Time',inplace=True)
magnit.to_excel('recData/MGNT_from_CSV_index.xlsx')

##GETTING DATA FROM WEB#####
tickers = "BRJ8"
startDate = '2018-1-1'
endDate = dt.datetime.today()
mgWeb = web.DataReader(tickers,'moex',startDate,endDate)
mgWeb.to_excel('recData/BRENT_FUTURE_from_web.xlsx')

####GETTING DATA FROM MICROSOFT####
tickers = ['^SPX']
dataSource = 'stooq'
startDate = '2018-1-1'
endDate = dt.datetime.today()
gWeb = web.DataReader(tickers,dataSource,startDate,endDate)
gWeb.to_excel('recData/SP500_from_web.xlsx')

worldBank = wb.download(indicator='NY.GDP.MKTP.CD',country=['RU'],start=2005,end=2008)
worldBank.to_excel('recData/WB_from_web.xlsx')

keyIndicies = quandl.get('BANKRUSSIA/KEYECIND')
keyIndicies.to_excel('recData/CB_from_web.xlsx')

magnit = pd.read_csv('data/MGNT_59331.csv')
magnit.set_index('Time',inplace=True)
print(magnit)

Low = magnit['Low']/57
print(magnit.head(10))
print(magnit.tail(10))

magnitSorted = magnit.sort_values(by='Deals',ascending=False).head(5)
print(magnit.sort_values(by='Deals',ascending=False))
magnit['LowUSD'] = magnit['Low']/57

###GETTING DATA FROM WEB#####


tickers = "MGNT"
startDate = '2018-1-1'
endDate = dt.datetime.today()
mgWeb = web.DataReader(tickers,'moex',startDate,endDate)
mgWeb = mgWeb[mgWeb['BOARDID']=='TQBR']

mgWeb = mgWeb[['VALUE', 'OPEN', 'LOW']]
mgWeb = mgWeb.assign(LowInUSD = mgWeb['LOW']/57)
mgWeb = mgWeb.assign(Numbers = mgWeb['VALUE']/mgWeb['LOW'])
print(mgWeb)