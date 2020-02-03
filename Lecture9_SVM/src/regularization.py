from sklearn.datasets import make_blobs
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X, y = make_blobs(centers=2, random_state=4, n_samples=30)

# посмотрим на данные на графике
# plt.figure()
#
# plt.scatter(X[:,0][y==0], X[:,1][y==0], c="red", edgecolor='k', marker='o')
# plt.scatter(X[:,0][y==1], X[:,1][y==1], c="green", edgecolor='k', marker='^')
#
# plt.xlabel("x1")
# plt.ylabel("x2")
#
# plt.legend(["Класс 1", "Класс 2"])

#plt.show()

clf = svm.SVC(kernel='linear')
clf.fit(X,y)

# ax = plt.gca() #get current axes
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
#
# w = clf.coef_[0]
# a = -w[0] / w[1]
# xx = np.linspace(xlim[0], xlim[1])
# yy = a * xx - (clf.intercept_[0]) / w[1]
#
# plt.plot(xx, yy, 'k-')

#plt.show()

for C in [0.01, 10, 1000]:
    plt.figure()

    plt.scatter(X[:, 0][y == 0], X[:, 1][y == 0], c="red", edgecolor='k', marker='o')
    plt.scatter(X[:, 0][y == 1], X[:, 1][y == 1], c="green", edgecolor='k', marker='^')

    clf = svm.SVC(kernel='linear', C=C)
    clf.fit(X, y)

    print("Коэффициенты (С = %f):" % C)
    print(clf.coef_)

    ax = plt.gca()  # get current axes
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(xlim[0], xlim[1])
    yy = a * xx - (clf.intercept_[0]) / w[1]

    plt.plot(xx, yy, 'k-')
    plt.title("C = %f" % C)

    plt.show()
