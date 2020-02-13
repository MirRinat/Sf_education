import numpy as np
import matplotlib.pyplot as plt

reds = list(range(127,255,2))
greens = list(range(127,255,2))

x = []
y = []
colors = []
sizes = []

plt.style.use(['seaborn-dark'])

for redShade in reds:
    for greenShade in greens:
        x.append(redShade)
        y.append(greenShade)
        sizes.append(400)
        colors.append([redShade,greenShade,0])

colors = np.array(colors)


plt.scatter(x,y,c=colors/255.0, s = sizes)


borderLineX = list(range(120,270))
borderLineY = []

for x in borderLineX:
    borderLineY.append(-x+486)

plt.plot(borderLineX,borderLineY)

plt.show()