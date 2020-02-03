import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# добавим шума к каждому 5му y
y[::5] += 3 * (0.5 - np.random.rand(8))

svr = SVR(kernel='rbf', C=10, gamma='auto')
svr.fit(X, y)
y_rbf = svr.predict(X)

plt.scatter(X, y, color='green')
plt.plot(X, y_rbf, color='k', linewidth=2)

plt.xlabel('data')
plt.ylabel('target')

plt.title('Support Vector Regression')

plt.show()