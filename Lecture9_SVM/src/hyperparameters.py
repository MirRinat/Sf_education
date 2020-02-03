from sklearn.datasets import make_blobs
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from hpsklearn import HyperoptEstimator
from hyperopt import tpe

X, y = make_blobs(centers=2, random_state=4, n_samples=30)

fig, axes = plt.subplots(3,3,figsize=(15,10))

for ax,C in zip(axes, [0.1,1,1000]):
    for a,gamma in zip(ax, [0.1,1,10]):
        clf = svm.SVC(kernel='rbf', C=C, gamma=gamma).fit(X, y)

        a.tick_params(which='both', bottom=False, top=False, labelbottom=False)
        a.scatter(X[:, 0][y == 0], X[:, 1][y == 0], c="red", edgecolor='k', marker='o')
        a.scatter(X[:, 0][y == 1], X[:, 1][y == 1], c="green", edgecolor='k', marker='^')

        x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
        y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        Z = Z.reshape(xx.shape)
        a.contour(xx, yy, Z, colors='k', linewidths=0.5)

        a.set_title("C = %f, gamma = %f" % (C,gamma))


axes[0,0].legend(["Класс 1","Класс 2"], ncol=2, loc=(0.9,1.2))
plt.show()