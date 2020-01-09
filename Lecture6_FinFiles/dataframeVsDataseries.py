import numpy as np
import pandas as pd
import pandas_datareader.data as web

fromDate = '2011-04-30'
toDate = '2018-06-15'

dataFrame = web.DataReader("GS",'yahoo',fromDate,toDate)
print(dataFrame.head())

