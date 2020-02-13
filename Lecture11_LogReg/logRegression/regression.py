import numpy as np
import matplotlib.pyplot as plt

randX = np.random.randint( 120, 255, 200 )
randY = np.random.randint( 120, 255, 200 )

colors = []
sizes = []

for i in range(0,200):
    x = randX[i]
    y = randY[i]
    sizes.append(400)
    if x + y - 486 > 0:
        colors.append('yellow')
    else:
        colors.append('grey')

borderLineX = list(range(120,270))
borderLineY = []

for x in borderLineX:
    borderLineY.append(-x+486)

plt.plot(borderLineX,borderLineY)
plt.scatter(randX,randY,c=colors,s=sizes)
plt.show()

