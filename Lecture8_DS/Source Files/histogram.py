from basicGraphs import loadPrices
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

# spx = loadPrices('../data/^spx_d.csv')
# spx = spx[['Close']]
# spx = spx.assign( pctChange = spx.pct_change() )
#
# close = spx['pctChange'].values[1:]
#
# n,buckets,patches= plt.hist(close,50,facecolor='blue',normed=1)
# #
# mean = close.mean()
# std = close.std()
# mu = mean
# sigma = std
# #
# # print("Среднее значение {0}, стандартное отклонение {1}".format(mu,sigma))
# bestFitLine = mlab.normpdf(buckets,mu,sigma)
# plt.plot(buckets,bestFitLine,color='black')


spx = loadPrices('../data/^spx_d.csv')
spx = spx[['Close']]
minDate = spx.index.min()
maxDate = spx.index.max()

weekendIndex = pd.date_range(minDate,maxDate,freq='W')
# weekstartIndex = weekendIndex.shift(2,freq=pd.datetools.day)

spxW = spx.reindex(weekendIndex)
print(spxW)
spxW = spxW.dropna()
spxW = spxW.assign( pctChange = spxW.pct_change() )
close = spxW['pctChange'].values[1:]

n,buckets,patches= plt.hist(close,50,normed=1,facecolor='yellow', alpha =0.5)

mean = close.mean()
std = close.std()
mu = mean
sigma = std

print("Среднее значение {0}, стандартное отклонение {1}".format(mu,sigma))
bestFitLine = mlab.normpdf(buckets,mu,sigma)
plt.plot(buckets,bestFitLine,'r--')

normalDist = np.random.normal(mu,sigma,5000)
nND,bucketsND,patchesND = plt.hist(normalDist,50,normed=1)

bestFitLineND = mlab.normpdf(bucketsND,mu,sigma)
plt.plot(bucketsND,bestFitLineND)

#plot distributions
plt.axvline(x=mu)
plt.axvline(x=mu+2*sigma)
plt.axvline(x=mu-2*sigma)
plt.axvline(x=mu+6*sigma)
plt.axvline(x=mu-6*sigma)
plt.show()
