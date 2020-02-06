from sklearn.datasets import make_moons
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from plotting_func import plot_2d_separator, plot_tree_partition

# генерируем двухмерный датасет
X, y = make_moons(n_samples=200, random_state=42, noise=0.1)

data = pd.DataFrame(np.c_[y,X],columns=["target", "x1", "x2"])
# print(data.head())


# посмотрим на данные на графике
plt.figure()

plt.scatter(data[data["target"]==0]["x1"], data[data["target"]==0]["x2"], color="red", edgecolor='k')
plt.scatter(data[data["target"]==1]["x1"], data[data["target"]==1]["x2"], color="green", edgecolor='k')

plt.xlabel("x1")
plt.ylabel("x2")

plt.show()

# построим случайный лес с 5 деревьями; в реальной жизни деревьев обычно сотни или даже тысячи
# forest = RandomForestClassifier(n_estimators=5, random_state=42)
# forest.fit(X,y)

# fig, axes = plt.subplots(2,3, figsize=(20,10))
#
# for i, (ax,tree) in enumerate(zip(axes.ravel(), forest.estimators_)):
#     ax.scatter(data[data["target"] == 0]["x1"], data[data["target"] == 0]["x2"], color="red", edgecolor='k')
#     ax.scatter(data[data["target"] == 1]["x1"], data[data["target"] == 1]["x2"], color="green", edgecolor='k')
#     plot_tree_partition(X, y, tree, ax=ax)
#     ax.set_title("Дерево {}".format(i+1))
#
# plot_2d_separator(classifier = forest, X=X, fill=True, ax=axes[-1,-1], alpha=0.4)
# axes[-1,-1].set_title("Лес")
# axes[-1,-1].scatter(data[data["target"] == 0]["x1"], data[data["target"] == 0]["x2"], color="red", edgecolor='k')
# axes[-1,-1].scatter(data[data["target"] == 1]["x1"], data[data["target"] == 1]["x2"], color="green", edgecolor='k')
#
# plt.show()

# информативность (важность) атрибутов x1 и x2
# print("Важность атрибутов x1 и x2: ", forest.feature_importances_)
#
# n_features = X.shape[1]
# plt.barh(range(n_features), forest.feature_importances_)
# plt.yticks(np.arange(n_features), ["x1", "x2"])
# plt.xlabel("Важность атрибута")
#
# plt.show()