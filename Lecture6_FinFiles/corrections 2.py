import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from pandas_datareader import wb

#ИСПОЛЬЗУЙТЕ yahoo, iex, stooq

# Загрузить акции Майкорософт
startDate = dt.datetime(2015, 1, 1)
endDate = dt.datetime.today()

MSFT = web.DataReader('MSFT','iex', startDate, endDate)
print(MSFT)


MSFTTwo = web.DataReader('MSFT','stooq',startDate,endDate)
print(MSFTTwo)
MSFTTwo = MSFTTwo[(MSFTTwo.index > startDate) & (MSFTTwo.index < endDate)]
print(MSFTTwo)
