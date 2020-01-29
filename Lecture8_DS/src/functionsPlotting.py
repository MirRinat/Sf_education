import matplotlib.pyplot as plt

from mysteryFunctions import mysteryFunctionOne, mysteryFunctionTwo

input = list(range(-20,20))

result = mysteryFunctionTwo(input)
plt.title("График супер секретной функции")
plt.scatter(input,result)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('zero')#koordinatnye linii ustanavlivaem poseredine
ax.spines['bottom'].set_position('zero')

#Убирваем границу сверху и снизу
ax.spines['right'].set_position('zero')
ax.spines['top'].set_position('zero')


plt.scatter(input,result)
plt.grid()
plt.show()