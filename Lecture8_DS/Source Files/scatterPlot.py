import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('../data/sf_pe_salaries_2011.csv')
#data = data.reindex(data['Id'])
data['BasePay'] = data['BasePay'].replace('Not Provided','0')

data['BasePay'] = data['BasePay'].astype(float)
data = data.fillna(0)
data = data.drop("Id",1)
print(data)

# Xaxis = data.index
# XaxisPercentile = data.index/data.index.max()*100
# Yaxis = data['BasePay'].values
# YaxisSorted = sorted(Yaxis)
#
# plt.scatter(XaxisPercentile,YaxisSorted)
# plt.grid()
# plt.show()

basePay = data['BasePay'].values
print("До очистки:",len(basePay))
basePay = basePay[basePay>1000]
print("После очистки:",len(basePay))

step = 20000
buckets = list( range( 1000, int( basePay.max() ),step ) )
chelikovInBuckets = []
for bucketStart in buckets:
    bucketEnd = bucketStart + step
    kol_vo = basePay[ (basePay>bucketStart) & (basePay<bucketEnd) ]
    chelikovInBuckets.append(len(kol_vo))

Xaxis = buckets
Yaxis = chelikovInBuckets

plt.plot(Xaxis,Yaxis)
plt.show()
