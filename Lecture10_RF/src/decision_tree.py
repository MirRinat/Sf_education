from sklearn.datasets import make_moons
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
import matplotlib.pyplot as plt
from plotting_func import plot_2d_separator

# генерируем двухмерный датасет
X, y = make_moons(n_samples=200, random_state=42, noise=0.1)

data = pd.DataFrame(np.c_[y,X],columns=["target", "x1", "x2"])
print(data.head())


# посмотрим на данные на графике
plt.figure()

plt.scatter(data[data["target"]==0]["x1"], data[data["target"]==0]["x2"], color="red", edgecolor='k')
plt.scatter(data[data["target"]==1]["x1"], data[data["target"]==1]["x2"], color="green", edgecolor='k')

plt.xlabel("x1")
plt.ylabel("x2")

# plt.show()


# построим решающее дерево
tree = DecisionTreeClassifier()
tree.fit(X,y)

print("Глубина чистого дерева: ", tree.tree_.max_depth)

export_graphviz(tree, out_file="../data/tree.dot", class_names=["red", "green"], feature_names = ["x1", "x2"], impurity=False)

with open("../data/tree.dot") as f:
    tree_graph = f.read()

graphviz.Source(tree_graph, filename="../data/tree", format='png').view()

plot_2d_separator(classifier = tree, X=X, fill=True, alpha=0.4)
plt.show()