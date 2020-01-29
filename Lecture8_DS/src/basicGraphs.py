import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def loadPrices(filename):
    data = pd.read_csv(filename)
    data = data.set_index(pd.DatetimeIndex(data['Date']))#устанавливаем индекс
    data = data.drop('Date', 1)#удаляем колонку
    return (data)


def normilizeValues(table,newColumn,existingColumn):
    priceAt0 = table.iloc[-1][existingColumn]
    #print(priceAt0)
    table[newColumn] = table.apply(lambda row:(row[existingColumn]/priceAt0),axis = 1)
    return table

# def normilizeValue(data,newColumn,existingColumn):
#     priceAt0 = data.iloc[-1][existingColumn]
#     print(priceAt0)
#     #data[newColumn] = data.apply(lambda row: (row[existingColumn]))

#
# oil = loadPrices('../Data/oilPrices.csv')
# usdRubPrice = loadPrices('../Data/usdPrices.csv')
#
# commonIndex = oil.index
# usdRubPrice = usdRubPrice.reindex(commonIndex)#сравнивание индексов с oil
# usdRubPrice = usdRubPrice.fillna(method='backfill')
# usdRubPrice = normilizeValues(usdRubPrice,'normilizeValue','Price')
# oilPrice = normilizeValues(oil,'normilizeValue','Price')
# # #x - index
# Xaxis = oil.index
# #
# # #y - price
# OilYaxis = oil['normilizeValue'].values
# RubYaxis = usdRubPrice['normilizeValue'].values
# #
# #
# #
# plt.plot(Xaxis,OilYaxis,color="red",label='Oil Price')
# plt.plot(Xaxis,RubYaxis,'b--',label='Rub Price')
# plt.legend()
# plt.show()
