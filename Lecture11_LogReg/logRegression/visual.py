import numpy as np
import matplotlib.pyplot as plt

randomY = np.random.randint(-20,20,100)

randomNegative = np.random.randint(-20,-1,100)
randomPositive = np.random.randint( 1,20,100)

plt.scatter(randomNegative,randomY)
plt.scatter(randomPositive,randomY)

y = list(range(-20,20))
x = np.zeros(len(y))

plt.plot(x,y)
plt.show()