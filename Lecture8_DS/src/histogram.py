#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import pandas as pd
from Lecture8_DS.src.basicGraphs import loadPrices
import numpy as np

# spx = loadPrices('../Data/^spx_d.csv')
# spx = spx[['Close']]
# spx = spx.assign(pctChange=spx.pct_change()) #добавление новой колонки
# #
# # # print(spx)
# close = spx['pctChange'].values[1:]
# # print(close)
# n,buckets,patches = plt.hist(close, 50, facecolor='blue', density=1)
# #
# mean = close.mean()
# std = close.std()
# mu = mean
# sigma = std
# #
# # print("Среднее отклонение {0},стандартное отклонение {1}".format(mu,sigma))
# bestFitLine = norm.pdf(buckets,mu,sigma)
# plt.plot(buckets,bestFitLine,'y--')
# plt.show()
 ##################################################
spx = loadPrices('../Data/^spx_d.csv')
spx = spx[['Close']]

minDate = spx.index.min()
maxDate = spx.index.max()

weekendIndex = pd.date_range(minDate, maxDate,freq='W')
weekstartIndex = weekendIndex
print(weekstartIndex)
spxW = spx.reindex(index=weekstartIndex)
print(spx)
print(spxW)
spxW = spxW.dropna()
spxW = spxW.assign(pctChange=spxW.pct_change())
close = spxW['pctChange'].values[1:]

n,buckets,patches = plt.hist(close, 50,normed=1,facecolor='yellow',alpha=0.5)

mean = close.mean()
std = close.std()
mu = mean
sigma = std
# print(spxW)
# print("Среднее значение {0}, стандартное отклонение {1}".format(mu,sigma))
bestFitLine = norm.pdf(buckets,mu,sigma)
plt.plot(buckets,bestFitLine,'r--')
# plt.show()

normalDist = np.random.normal(mu,sigma,20000)
nND,bucketsND,patchesND = plt.hist(normalDist,50,normed=1)
bestFitLineND = norm.pdf(bucketsND,mu,sigma)
plt.plot(bucketsND,bestFitLineND)
plt.axvline(x=mu)
plt.axvline(x=mu+2*sigma)
plt.axvline(x=mu-2*sigma)
plt.axvline(x=mu+6*sigma)
plt.show()
