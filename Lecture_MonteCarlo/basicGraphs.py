import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def loadPrices(fileName):
    data = pd.read_csv(fileName)
    data = data.set_index(pd.DatetimeIndex(data['Date']))
    data = data.drop('Date', 1)
    return data

#price@t0 = 100%
def normalizeValues(table,newColumn,existingColumn):
    priceAtT0 = table.iloc[-1][existingColumn]
    table[newColumn] = table.apply(lambda row: (row[existingColumn]/priceAtT0), axis = 1)

    return table


# oil = loadPrices('../data/oilPrices.csv')
# usdRubPrice = loadPrices('../data/usdPrices.csv')
#
# #re-index index USD = index Oil
# commonIndex = oil.index
# usdRubPrice = usdRubPrice.reindex(commonIndex)
# usdRubPrice = usdRubPrice.fillna(method='backfill')
#
# #normalizing values
# usdRubPrice = normalizeValues(usdRubPrice,'normalizedValue','Price')
# oil = normalizeValues(oil,'normalizedValue','Price')
#
#
#
# Xaxis = commonIndex
# # #Y = price
# OilYaxis = oil['normalizedValue'].values
# RubYAxis = usdRubPrice['normalizedValue'].values
#
# #
# #
# #
# plt.plot(Xaxis,OilYaxis,color="red", label='Oil Price')
# plt.plot(Xaxis,RubYAxis, 'b--', label='Цена рублика')
# plt.legend()
# plt.show()


