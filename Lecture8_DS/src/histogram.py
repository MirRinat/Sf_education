import matplotlib.pyplot as plt
from basicGraphs import loadPrices
import pandas

spx = loadPrices('../Data/^spx_d.csv')
spx = spx[['Close']]
spx = spx.assign(pctChange=spx.pct_change()) #добавление новой колонки

print(spx)
close = spx['pctChange￿'].values[1:]

plt.hist(close, 50)
plt.show()