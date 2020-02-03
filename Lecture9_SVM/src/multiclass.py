from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X,y = make_blobs(random_state=42)

# посмотрим на данные на графике
plt.figure()

plt.scatter(X[:,0][y==0], X[:,1][y==0], c="red", edgecolor='k', marker='o')
plt.scatter(X[:,0][y==1], X[:,1][y==1], c="green", edgecolor='k', marker='^')
plt.scatter(X[:,0][y==2], X[:,1][y==2], c="blue", edgecolor='k', marker='v')

plt.xlabel("x1")
plt.ylabel("x2")

plt.legend(["Класс 1", "Класс 2", "Класс 3"])

#plt.show()

clf1 = LinearSVC(multi_class='ovr')  # стратегия one-vs-rest
clf1.fit(X,y)

print("Количество коэффициентов (OvR): ", clf1.coef_.shape)
print("Количество интерцептов (OvR): ", clf1.intercept_.shape)

# посмотрим на разделяющие линии

# line = np.linspace(-15,15)
# for coef, intercept, color in zip(clf1.coef_, clf1.intercept_, ['red', 'green', 'blue']):
#     plt.plot(line, -(line*coef[0] + intercept)/coef[1], c=color)
# plt.ylim(-10,15)
# plt.xlim(-10,15)
# plt.show()

clf2 = SVC(kernel='linear', decision_function_shape='ovo')  # стратегия one-vs-one
clf2.fit(X,y)

print("Количество коэффициентов (OvO): ", clf2.coef_.shape)
print("Количество интерцептов (OvO): ", clf2.intercept_.shape)

# посмотрим на разделяющие линии

line = np.linspace(-15,15)
for coef, intercept, color in zip(clf2.coef_, clf2.intercept_, ['brown', 'cyan', 'purple']):
    plt.plot(line, -(line*coef[0] + intercept)/coef[1], c=color)
plt.ylim(-10,15)
plt.xlim(-10,15)
plt.show()
