#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import pandas as pd
from pandas import datetools
import datetime
from datetime import timedelta
from Lecture8_DS.src.basicGraphs import loadPrices
import statsmodels.stats.api as sms

# spx = loadPrices('../Data/^spx_d.csv')
# spx = spx[['Close']]
# spx = spx.assign(pctChange=spx.pct_change()) #добавление новой колонки
#
# # print(spx)
# close = spx['pctChange'].values[1:]
# # print(close)
# n,buckets,patches = plt.hist(close, 50,normed=1)
#
# mean = close.mean()
# std = close.std()
# mu = mean
# sigma = std
#
# print("Среднее отклонение {0},стандартное отклонение {1}".format(mu,sigma))
# bestFitLine = norm.pdf(buckets,mu,sigma)
# plt.plot(buckets,bestFitLine,'y--')
# plt.show()

spx = loadPrices('../Data/^spx_d.csv')
spx = spx[['Close']]
minDate = spx.index.min()
maxDate = spx.index.max()
# print(minDate, maxDate)
weekendIndex = pd.date_range(minDate, maxDate,freq='W')
weekstartIndex = weekendIndex.shift(1, freq=pd.datetools.day)
# print(weekstartIndex)

spxW = spx.reindex(weekstartIndex)
print(spxW)
