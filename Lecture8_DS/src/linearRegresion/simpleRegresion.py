import matplotlib.pyplot as plt
import numpy as np
from Lecture8_DS.src.mysteryFunctions import mysteryFunctionTwo, mysteryFunctionSmall, mysteryFunctionLarge

input = list(range(-100,200))

result = mysteryFunctionLarge(input)
mathFunction = mysteryFunctionTwo(input)
plt.title("График супер секретной функции")



Xactual = np.array(input)
Yactual = np.array(result)

denominator = Xactual.dot(Xactual) - Xactual.mean() * Xactual.sum()
m = (Xactual.dot(Yactual) - Yactual.mean()*Xactual.sum())/denominator
b = (Yactual.mean() *Xactual.dot(Xactual) - Xactual.dot(Yactual) *Xactual.mean())/denominator

Ypredictor = m*Xactual + b

plt.scatter(input,result)
plt.plot(input,Ypredictor,'r')
plt.plot(input,mathFunction,'y--')

#r2
predDiff = Yactual - Ypredictor
avgDiff = Yactual - Yactual.mean()
r2 = 1 - (predDiff.dot(predDiff)/avgDiff.dot(avgDiff))
print('r2 для нашей модели',r2)
plt.grid()
plt.show()