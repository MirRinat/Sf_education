import numpy as np
import pandas as pd
import pandas_datareader.data as web

fromDate = '2011-04-30'
toDate = '2018-06-15'

dataFrame = web.DataReader("GS",'yahoo',fromDate,toDate)
dataSeries = dataFrame['Close']
dataFrameOne = dataFrame[['Close']]
dataFrameOne['CloseInRub'] = dataFrameOne['Close'] * 66
print(dataSeries.head())
print(dataFrameOne.head())

#Разница между dataframe и dataSeries - два разных объекта,с одинковыми данными,но разным функционалом
#dataFrame - это коллекция,массив данных,состоящий из dataseries