import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import quandl
from pandas_datareader import wb
###GETTING DATA####
# magnit = pd.read_csv('Data/MGNT_191201_200101.csv')
# magnit.set_index('<DATE>',inplace=True)
# magnit.to_excel('recData/MGNT_from_csv_index.xlsx')

# ###Getting data from web###
# tickers = "MGNT"
# startDate = '2020-1-1'
# endDate = dt.datetime.today()
# mgWeb = web.DataReader(tickers,'moex',startDate,endDate)
# mgWeb.to_excel('recData/MGNT_from_web.xlsx')
#
# ##Getting data from microsoft
# tickers = ['MSFT', 'AAPL']
# dataSource = 'stooq'
# #google don't get the info
# startDate = '2018-1-1'
# endDate = dt.datetime.today()
# gWeb = web.DataReader(tickers,dataSource,startDate,endDate)
# gWeb.to_excel('recData/Google_APPL_from_web.xlsx')
#
# worldBank = wb.download(country='RU',indicator='NY.GDP.MKTP.CD',start=2010,end=2018)
# worldBank.to_excel('recData/GDP_RU_from_web.xlsx')
# ##QUANDL###
# keyIndicies = quandl.get('BANKRUSSIA/KEYECIND')
# keyIndicies.to_excel('recData/CB_from_web.xlsx')
# ##MAGNIT sort,head
# magnit = pd.read_csv('data/MGNT_191201_200101.csv')
# magnit.set_index('Time',inplace=True)
# print(magnit)
#
# Low = magnit['Low']/57
# print(magnit.head(10))
# print(magnit.tail(10))
#
# magnitSorted = magnit.sort_values(by='Deals',ascending=False).head(5)
# print(magnit.sort_values(by='Deals',ascending=False))
# magnit['LowUSD'] = magnit['Low']/57

###GETTING DATA FROM WEB#####


tickers = "MGNT"
startDate = '2018-1-1'
endDate = dt.datetime.today()
mgWeb = web.DataReader(tickers,'moex',startDate,endDate)
mgWeb = mgWeb[mgWeb['BOARDID'] == 'TQBR']
print(mgWeb.index)
print(mgWeb.columns)
mgWeb = mgWeb[['VALUE', 'OPEN', 'LOW']]
mgWeb = mgWeb.assign(LowInUSD = mgWeb['LOW']/57)
mgWeb = mgWeb.assign(Numbers = mgWeb['VALUE']/mgWeb['LOW'])
print(mgWeb)