# 1 point
# создайте функцию exampleOne с одним входным параметром
# входной параметр есть массив чисел
# возведите каждый элемент в квадрат и верните их в новом массиве
def exampleOne(array):
    myarray = []
    for i in array:
        myarray.append(i * i)
    return myarray


# 2 points
# создайте функцию exampleTwo с одним входным параметром
# входной параметр есть массив чисел
# верните два последних элемента в новом массиве с 100 добавленных к каждому из них
# т.е. [1,2,3] -> [102,103]
def exampleTwo(array):
    myarray = []
    myarray.append(array[-2] + 100)
    myarray.append(array[-1] + 100)
    return (myarray)


# 2 points
# создайте функцию exampleThree с одним входным параметром
# входной параметр есть массив случайных значений
# верните четные элементы массива т.е. 2ой, 4ый, 6ой, и т.д.
def exampleThree(array):
    myarray = []
    for i in range(1, len(array), 2):
        myarray.append(array[i])
    return myarray


# 5 points
# создайте функцию exampleFour с двумя входными параметрами
# первый входной параметр есть массив чисел, второй единственное число
# если элемент равен 7 и 12 -- сразу же прекратите выполнение цикла
# если элемент делится на второй входной параметр без остатка, добавьте его в массив для возврата
# убедитесь что каждый элемент в массиве для возврата является текстом, а не числом
# верните трансформированный массив
# подсказка: остаток считается через %, т.е. 7%2 = 1
def exampleFour(array, num):
    myarray = []
    for i in array:
        if str(i).isdigit:
            if i == 7 or i == 12:
                break
            if i % num == 0:
                myarray.append(str(i))
    return myarray
#
# print(["3","9","6"] == exampleFour([3,5,9,6,7,15,24],3))
# print(exampleFour([3,5,9,6,7,15,24],3))
# print(["4","2","6","6"] == exampleFour([4,1,2,6,5,6,12],2))
# print(exampleFour([4,1,2,6,5,6,12],2))
# print(["4","2","6","6"])