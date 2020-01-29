import pandas
import matplotlib.pyplot as plt
import numpy

data = pandas.read_csv('../Data/sf_pe_salaries_2011.csv')
data = data.reindex(data['Id'])
data['BasePay'] = data['BasePay'].replace('Not Provided','0')
data['BasePay'] = data['BasePay'].astype(float)
data = data.fillna(0)
data = data.drop('Id',1)
print(data)

# Xaxis = data.index
# XaxisPercent = data.index/data.index.max()*100
# Yaxis = data['BasePay'].values
# YaxisSorted = sorted(Yaxis)
#
# plt.scatter(XaxisPercent,YaxisSorted)
# plt.grid()
# plt.show()

basePay = data['BasePay'].values
print(len(basePay))
basePay = basePay[basePay > 1000]
print(len(basePay))

step = 20000
buskets = list(range(1000,int(basePay.max() ),step))
chelBuckets = []
for busketStart in buskets:
    busketEnd = busketStart +step
    kol_vo = basePay[(basePay>busketStart) & (basePay<busketEnd)]
    chelBuckets.append((len(kol_vo)))

Xaxis = buskets
Yaxis = chelBuckets

plt.plot(Xaxis,Yaxis)
plt.show()