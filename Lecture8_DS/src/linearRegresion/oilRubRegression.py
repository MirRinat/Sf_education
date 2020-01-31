#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import  linear_model
from sklearn.metrics import r2_score
oil = pd.read_csv('../../Data/oilPrices.csv',index_col='Date',parse_dates=True)
usdRub = pd.read_csv('../../Data/usdPrices.csv',index_col='Date',parse_dates=True)
# print(usdRub)
# print("first set",oil)
oilTrain = oil[(oil.index>datetime.datetime(2014,9,1)) & (oil.index<datetime.datetime(2016,4,1))]
usdRubTrain = usdRub[(usdRub.index>datetime.datetime(2014,9,1)) & (usdRub.index<datetime.datetime(2016,4,1))]

oilTest = oil[(oil.index>datetime.datetime(2016,4,1)) & (oil.index<datetime.datetime(2018,4,1))]
usdRubTest = usdRub[(usdRub.index>datetime.datetime(2016,4,1)) & (usdRub.index<datetime.datetime(2018,4,1))]
# print("selected set",[oilTrain)
#приведение к  одному размеру осей и точек
commonIndex = oilTrain.index
usdRubTrain = usdRubTrain.reindex(commonIndex)
usdRubTrain = usdRubTrain.fillna(method='backfill')


commonIndexTest = oilTest.index
usdRubTest = usdRubTest.reindex(commonIndexTest)
usdRubTest = usdRubTest.fillna(method='backfill')


#x = oil
#y = usdRub

Xtrain = oilTrain['Price'].values
Ytrain = usdRubTrain['Price'].values

Xtest = oilTest['Price'].values
Ytest = usdRubTest['Price'].values


plt.scatter(Xtest,Ytest,color='red')

Xtest = Xtest.reshape(len(Xtest),1)
Ytest = Ytest.reshape(len(Ytest),1)

regr = linear_model.LinearRegression()
Xtrain = Xtrain.reshape(len(Xtrain),1)
Ytrain = Ytrain.reshape(len(Ytrain),1)

regr.fit(Xtrain,Ytrain)
print(regr.intercept_)#b
print(regr.coef_)#m   y=mx+b

Ytestpredicted = regr.predict(Xtest)
Ytrainpredicted = regr.predict(Xtrain)

trainErrors = Ytrainpredicted-Ytrain#помимо r2 показывает качество предсказания
print("среднее значение ошибки для 2014 - 2016",trainErrors.mean())

testErrors = Ytestpredicted-Ytest
print("среднее значение ошибки для 2016 - 2018",testErrors.mean())

plt.plot(Xtest, Ytestpredicted)

r2test = r2_score(Ytest,Ytestpredicted)
r2train = r2_score(Ytrain, Ytrainpredicted)#показывает качество предсказания
print("r2 связи доллара от нефти 2016-2018",r2test)
print("r2 связи доллара от нефти 2014-2016",r2train)
# plt.show()
