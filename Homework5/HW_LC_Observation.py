#Этот файл дает вам возможность попробовать различные концепции самостоятельно,
#понять как они работают и разобраться с ними перед тем, как начнёте выполнять
#домашнее задание на оценку.
#Как я и говорил во время занятия, вам нужно:
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


#UC: есть несколько вариантов, когда мы можем сравнивать результаты различный операций
#print("equals"=="equals")
#print("equals"=="not equals")
#Как вы могли убедиться на примере наверху есть два типа логических значений
#правда -- true, ложь -- false
#UC: можно комбинировать эти значения для получения более сложных кондиций
#print("equals"=="equals" and "this"=="this")
#это будет true только если первое И(AND) второе значение будет true
#print("equals"=="equals" and "this"=="that")
#если один из параметров не true то все выражение будет неправдой
#UC: так же есть операций ИЛИ(OR)
#print("equals"=="equals" or "this"=="that")
#это будет true только если первое ИЛИ(OR) второе значение будет true
#UC: также можно использовать отрицание
#print("this" != "that")
#это будет true потому что "THIS НЕ РАВНО THAT"
#UC: тоже можно применять к более сложным конструкциям при помощи not
#print(not("equals"=="equals" and "this"=="that"))
#UC: в основном данные конструкции применяются с if
##if( "this" == "that"): print("Not true, so nothing")
##if( "this" != "that"): print("True, so something")
#UC: нужно быть очень аккуратными, когда работаем с выходами из if
##value = ""
##if( "this" == "this"):
##    value = "This equals this"
##value = "This equals that"
##print(value)
#даный код не дает правильные результат, потому что результат if
#переписан на предыдущих строчках, поэтому мы должны использовать
#if-else
##value = ""
##if( "this" == "this"):
##    value = "This equals this"
##else: value = "This equals that"
##print(value)
#WC: создайте аррай testArray со значениями one,two,three
#UC: чтобы проверить если элемент находиться в array, то
#нужно использовать in
##print( "one" in testArray )
##print( "five" in testArray )
#WC: создайте текстовую перменную testString с текстом "testContains"
#UC: так же можно посмотреть если какой-то текст находится внутри строки
##print("test" in testString)
##print("Contains" in testString)
##print("something" in testString)



