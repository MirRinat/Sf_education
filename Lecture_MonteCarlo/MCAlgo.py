from basicGraphs import loadPrices
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

tries = 100000
slots = 37

ruletockaNumbers = np.random.randint(0, slots, tries)

# count, bins, patches = plt.hist(ruletockaNumbers,slots)
average = np.full(slots+1, tries/slots)
# print(average)

# plt.plot(bins, average,'r--',linewidth=2)
# plt.show()

#
# bookofResults = {}
# for result in ruletockaNumbers:
#     currentCount = bookofResults.get(result,0)
#     bookofResults[result] = currentCount + 1
#
# mathematicallyExpected = 1/slots
# probabillityOfAnyResult = bookofResults[13]/tries
# print("real number ",probabillityOfAnyResult,"vs ",mathematicallyExpected)

gs = loadPrices('../data/GS.csv')
gs = gs.assign(pctChange = gs.pct_change())
pctChange = gs['pctChange '].value[1:]

mu = pctChange.mean()
sigma = pctChange.std()

n,buckets,patches = plt.hist(pctChange,50,normed=1,facecolor='green')
bestFitLine = mlab.normpdf(buckets,mu,sigma)
plt.plot(buckets,bestFitLine,'r--')
