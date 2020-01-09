# Этот файл дает вам возможность попробовать различные концепции самостоятельно,
# понять как они работают и разобраться с ними перед тем, как начнёте выполнять
# домашнее задание на оценку.
# Как я и говоорил во время занятия, вам нужно:
#   1.Прочитать строчку которая начинается с  "#" -- это ваша инструкция.
#   2.Данная строчка скажет вам что делать. Это может быть:
#          a)Убрать коммент(UC) со следующей строчки с "##" -- это строчка кода.
#          b)Написать(WC) простейший код самим
#   3.Рекомендую закоментить текущую строчки кода при переходе к следущему заданию,
#     чтобы было проще.
# Я специально сделал эти задачи повторящими то, что мы прошли в классе,
# для того, чтобы вы могли попробовать код одни.
# Удачи!

# Цикл работает с каждым элементом в коллекции
# WC: создайте массив myArray с 5 элементами в нем:

# UC: есть два способа итерации через массив
# певый: просто для каждого элемента
## for element in myArray:
##     print(element)
# второй: воспользоваться индексом внутри массива:
## for i in range(0,len(myArray)):
##     print( myArray[i] )

#А зачем нам итерация с использованием индекса?
#UC: a) так вы можете работать только с частью массива, например первые три элемента
## for i in range(0,3):
##     print(myArray[i])

#UC: b) так же вы можете понять на какой позиции находится определенный элемент
## toCheck = "somethingOfInterest"
## myArray.append(toCheck)
## for i in range(0,len(myArray)):
##     if(myArray[i]) == toCheck:
##         print("The position of the element is: ", i)

#UC: вы так же можете одновременно получить доступ и к элементу и к индексу:
## for index,value in enumerate(myArray):
##     print(index,value)

#One can also either interrupt or force loop to go to the next value
#Вы так же можете прервать цикл или заставить цикл перейти к следующему значению
#UC: прерывание цикла осуществляется через слово break (как break the loop)
## myArray.append("randomElement1")
## myArray.append("randomElement2")
## finalResult = []
## for element in myArray:
##     if "randomElement1" == element: break
##     finalResult.append(element)

# print("Прерванный цикл создал: ", finalResult)
#UC: сравните это с результатом непрерванным циклом
## finalResult = []#emptying the array
## for element in myArray:
##     finalResult.append(element)
##
# print("Непрерванный цикл создал:  ", finalResult)

#Так же можно заставить цикл перейти к следующему элементу без выполнения оставшегося кода в цикле
#UC: заставить цикл пропустить третий и четвертый элемент синтаксисом continue( как continue to the next element )
## for i in range(0,len(myArray)):
##     if i == 2 or i == 3: continue
##     #код внизу не будет выполнен для 3 и 4 элемента
##     finalResult.append(myArray[i])

# print("Результат использования 'continue' в коде: ", finalResult)
#сравните этот результат с непрерванным результатом навреху

#UC: вы также можете использовать цикл внутри цикла. КРАЙНЕ ВНИМАТЕЛЬНО ПОСМОТРИТЕ РЕЗУЛЬТАТ
## newArray = ["Unum","Duo","Tres","Quattuor"]
## for outerElement in myArray:
##     for innerElement in newArray:
##         print("Outer element {} and inner element {}".format(outerElement,innerElement))







