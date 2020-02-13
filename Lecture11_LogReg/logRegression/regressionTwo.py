import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['seaborn-dark'])

def sigmoid(x):
    return 1/(1+np.math.exp(-x))

borderLineX = list(range(200,270))
borderLineY = []

for x in borderLineX:
    borderLineY.append(-x+486)

plt.plot(borderLineX,borderLineY)

reds = list( range(200,255))
greens = list( range(200,255,1))

x = []
y = []
colors = []
sizes = []

for redShade in reds:
    for greenShade in greens:
        x.append(redShade)
        y.append(greenShade)
        sizes.append(150)
        probability = sigmoid(redShade+greenShade-486)
        colors.append( [ round(255*probability), round(255*probability) ,0])

colors = np.array(colors)

plt.scatter(x,y,c=colors/255.0, s = sizes)
plt.show()