#Этот файл дает вам возможность попробовать различные концепции самостоятельно,
#понять как они работают и разобраться с ними перед тем, как начнёте выполнять
#домашнее задание на оценку.
#Как я и говоорил во время занятия, вам нужно:
#   1.Прочитать строчку которая начинается с  "#" -- это ваша инструкция.
#   2.Данная строчка скажет вам что делать. Это может быть:
#          a)Убрать коммент(UC) со следующей строчки с "##" -- это строчка кода.
#          b)Написать(WC) простейший код самим
#   3.Рекомендую закоментить текущую строчки кода при переходе к следущему заданию,
#     чтобы было проще.
#Я специально сделал эти задачи повторящими то, что мы прошли в классе,
#для того, чтобы вы могли попробовать код одни.
#Удачи!

########################################################################
########################################################################

#This file exists for you to try different things,
#understand how they work and get confident with concepts
#before jumping to doing for score homework.
#As i have mentioned during the class, do the following:
#   1.Read the line with single "#" in front -- this is an instruction.
#   2.What you read will tell you what to do .It is either:
#          a)Uncomment(UC) line that starts with "##"(code line)
#          b)Write(WC) simple code by yourself.
#   3.Once you done, comment the created or uncommented line to keep things neat
#I specifically made it to mirror largely what we cover in the class,
#but to give you an opportunity to try things by yourself.
#Good Luck
########################################################################
########################################################################
#WC: создайте array goodies со значениями: money, power, glory, dignity, success

#UC:
##print(goodies)

#UC: порядковый номер каждого элемента
##for index,value in enumerate(goodies):
##    print(index,value)

#UC: выведет первый элемент из array, помните, нумерация с нуля
##print(goodies[0])

#UC: вы получите кол-во элементов в array
##print(len(goodies))

#UC: будет ошибка, потому что элементов 6, а нумерация идёт с 0 до 5
#print(goodies[len(goodies)])

#UC: это будет работать и даст последний элемент. закоменьте строчку наверху
##print(goodies[len(goodies)-1])

#UC: можно сократить до строчки внизу.
# строчка внизу и наверху дает одинаковый результат
##print( goodies[-1] )

#UC: код внизу заменяет 1-ый элемент(под индексом 0)
##goodies[0] = 'wealth'
##print(goodies)

#WC: замените первый элемент обратно на love

##print(goodies)

#UC: код внизу даёт от и до
##print( goodies[1:4] )

#UC: c нуля до элемента 4
##print( goodies[:4] )

#UC: c 1 до последнего
##print( goodies[1:] )

#UC: код внизу добавит элемент к array
##goodies.append("laughter")
##print( goodies )

#WC: добавьте money к нашему array

#UC: посмотрите что получилось
##print( goodies )

#UC: код внизу убирает последний элемент
##goodies.pop()
##print(goodies)

#UC: убирает 3-ий элемент(под индексом 2)
##goodies.pop(2)
##print(goodies)

#WC: cоздайте array moreGoodies с элементами: travel, company

#UC: код внизу соединяет два array:
##print(goodies+moreGoodies)







