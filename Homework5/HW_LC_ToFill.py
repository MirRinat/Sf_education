# Заполните инструкции внизу
# Если вы видите в консоле "Process finished with exit code 0"
# запустите правильный файл _Test

#1 бал
#cоздайте функцию с именем exampleOne, у которой будет два входных параметра.
#верните True если они не одинаковы
def exampleOne(a,b):
    if a != b:
        return True
    return False
#1 бал
#cоздайте функцию с именем exampleTwo, у которой будет три входных параметра.
#верните True если все три параметра равны друг другу
def exampleTwo(a,b,c):
    if a == b == c:
        return True
    return False

#1 бал
#cоздайте функцию с именем exampleThree, у которой будет три входных параметра.
#верните True если первый отличен от второго, либо второй равен третьему
def exampleThree(a,b,c):
    if a != b or b == c:
        return True
    return False

#2 бала
#cоздайте функцию с именем exampleFour, у которой будут два текстовых входных параметра.
#если второй парметр является частью первого -- верните последнюю букву первого параметра
#если второй парметр не является частью первого -- верните первую букву первого параметра
#подсказка: любой текстовый элемент string -- это array букв
def exampleFour(a,b):
    if a.find(b) != -1:
        return a[-1]
    else:
        return a[0]

#2 бала
#cоздайте функцию с именем exampleFive, у которой будет три входных параметра: один array и два простых.
#верните "One", если первый элемент есть в array
#верните "Two", если второй элемент есть в array
#вените "None", если ни один из элементов не находиться в array
def exampleFive(array,one,two):
    for i in array:
        if i == one:
            return "One"
        elif i == two:
            return "Two"
    return "None"

#3 бала
#cоздайте функцию с именем exampleSix, у которой будет три входных параметра: один array и два простых.
#верните "Success" если второго элемента нет в array и количество элементов в array'е соответсвует третьему элементу
#верните "Not In Success" если второго элемента нет в array и количество элементов в array'е не соответсвует третьему элементу
#верните "Length Success" если второй элемент есть в array и количество элементов в array'е соответсвует третьему элементу
#верните "Failure" если второй элемент есть в array и количество элементов в array'е не соответсвует третьему элементу
def exampleSix(array,one, two):
    if one not in array and len(array) == two:
        return "Success"
    if one not in array and len(array) != two:
        return "Not In Success"
    if one in array and len(array) == two:
        return "Length Success"
    if one in array and len(array) != two:
        return "Failure"
# print([1,2,3,4,6].index(7))