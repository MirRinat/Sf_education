from sklearn.datasets import make_moons
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from src.plotting_func import plot_2d_separator, plot_tree_partition


# генерируем двухмерный датасет
X, y = make_moons(n_samples=200, random_state=42, noise=0.1)

fig, axes = plt.subplots(3,2,figsize=(15,10))

for ax,n_est in zip(axes, [5,50,500]):
    for a,max_f in zip(ax, [1,2]):
        clf = RandomForestClassifier(n_estimators=n_est, max_features=max_f, n_jobs=-1).fit(X, y)

        plot_2d_separator(classifier = clf, X=X, fill=True, ax=a, alpha=0.4)

        a.tick_params(which='both', bottom=False, top=False, labelbottom=False)
        a.scatter(X[:, 0][y == 0], X[:, 1][y == 0], c="red", edgecolor='k', marker='o')
        a.scatter(X[:, 0][y == 1], X[:, 1][y == 1], c="green", edgecolor='k', marker='^')

        a.set_title("n_estimators = %f, max_features = %f" % (n_est, max_f))

plt.show()