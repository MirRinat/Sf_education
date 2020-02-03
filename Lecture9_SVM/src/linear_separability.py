from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# генерируем двухмерный датасет
X, y = make_circles(n_samples=200, random_state=42, factor=0.5, noise=0.05)

data = pd.DataFrame(np.c_[y,X],columns=["target", "x1", "x2"])
print(data.head())


# посмотрим на данные на графике
plt.figure()

plt.scatter(data[data["target"]==0]["x1"], data[data["target"]==0]["x2"], color="red", edgecolor='k')
plt.scatter(data[data["target"]==1]["x1"], data[data["target"]==1]["x2"], color="green", edgecolor='k')

plt.xlabel("x1")
plt.ylabel("x2")

plt.show()


# добавим третье измерение: x3 = x1^2 + x2^2
data["x3"] = np.sqrt(data["x1"]**2 + data["x2"]**2)
print(data.head())


# график x3 и x2
# plt.figure()
#
# plt.scatter(data[data["target"]==0]["x3"], data[data["target"]==0]["x2"], color="red", edgecolor='k')
# plt.scatter(data[data["target"]==1]["x3"], data[data["target"]==1]["x2"], color="green", edgecolor='k')
#
# plt.xlabel("x3")
# plt.ylabel("x2")

#plt.show()

# график x3 и x1
# plt.figure()
#
# plt.scatter(data[data["target"]==0]["x3"], data[data["target"]==0]["x1"], color="red", edgecolor='k')
# plt.scatter(data[data["target"]==1]["x3"], data[data["target"]==1]["x1"], color="green", edgecolor='k')
#
# plt.xlabel("x3")
# plt.ylabel("x1")

#plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(data[data["target"]==0]["x1"], data[data["target"]==0]["x2"], data[data["target"]==0]["x3"], color="red", edgecolor='k')
# ax.scatter(data[data["target"]==1]["x1"], data[data["target"]==1]["x2"], data[data["target"]==1]["x3"], color="green", edgecolor='k')
#
# ax.set_xlabel('x1')
# ax.set_ylabel('x2')
# ax.set_zlabel('x3')
#
# plt.show()