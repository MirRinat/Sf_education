import matplotlib.pyplot as plt
import numpy as np
from Lecture8_DS.src.mysteryFunctions import mysteryFunctionTwo, mysteryFunctionSmall, mysteryFunctionLarge
from sklearn import  linear_model
from sklearn.metrics import r2_score
input = list(range(-100,200))

result = mysteryFunctionLarge(input)
mathFunction = mysteryFunctionTwo(input)
plt.title("График супер секретной функции")



Xactual = np.array(input)
Yactual = np.array(result)

denominator = Xactual.dot(Xactual) - Xactual.mean() * Xactual.sum()
m = (Xactual.dot(Yactual) - Yactual.mean()*Xactual.sum())/denominator
b = (Yactual.mean() *Xactual.dot(Xactual) - Xactual.dot(Yactual) *Xactual.mean())/denominator
print("наши собственные параметры",m,b)
Ypredictor = m*Xactual + b
#
plt.scatter(input,result)
plt.plot(input,Ypredictor,'r')
plt.plot(input,mathFunction,'y--')
#
# #r2
predDiff = Yactual - Ypredictor
avgDiff = Yactual - Yactual.mean()
r2 = 1 - (predDiff.dot(predDiff)/avgDiff.dot(avgDiff))
# print('r2 для нашей модели',r2)


# plt.grid()
# plt.show()

regr = linear_model.LinearRegression()
Xtrain = Xactual.reshape(len(Xactual),1)
Ytrain = Yactual.reshape(len(Yactual),1)

regr.fit(Xtrain,Ytrain)
Yeasypredicted = regr.predict(Xtrain)
r2easy = r2_score(Ytrain,Yeasypredicted)
print("r2 свяхи цены рубля от нефти",r2easy)
plt.plot(Xtrain,Yeasypredicted,color='grey')

plt.show()