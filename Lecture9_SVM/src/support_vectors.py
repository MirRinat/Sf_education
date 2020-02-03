import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import svm

# случайно генерируем положительные и отрицательные числа
rndY = np.random.randint(-20,20,100)
rndNeg = np.random.randint(-20,-1,100)
rndPos = np.random.randint(1,20,100)

dfNeg = pd.DataFrame(data=[rndNeg, rndY, np.zeros(100)]).T
dfPos = pd.DataFrame(data=[rndPos, rndY, np.ones(100)]).T

df = pd.concat([dfNeg,dfPos])

print(df.shape)
print(df.head())

# # тренируем линейный SVM-классификатор

clf = svm.SVC(kernel='linear')
clf.fit(df[[df.columns[0],df.columns[1]]], df[df.columns[2]])

# рисуем график

plt.scatter(df[df.columns[0]], df[df.columns[1]], c=df[df.columns[2]], cmap=plt.cm.Set3)

ax = plt.gca() #get current axes
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1])
yy = np.linspace(ylim[0], ylim[1])

YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# разделительная граница
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

print("Коэффициенты:")
print(clf.coef_)

print("Интерцепт:")
print(clf.intercept_)
#
# # опорные векторы
print("Опорные векторы:")
print(clf.support_vectors_)

ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], color='k', s=60, linewidth=1, facecolors='none')
plt.show()

