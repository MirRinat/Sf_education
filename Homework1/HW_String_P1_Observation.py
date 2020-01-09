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
#WC: Создайте текст "text" со значением 'abcde'
text = 'abcde'
#UC: Уберите коментарий чтобы вывести значение в консоль
print(text)
#WC: Создайте новую текстовую переменную "text2"  со значением "xyz"

#UC:  посмотрите результат
##print(text+text2)
#UC: можно комбинировать любые сочетания
##print(text+" "+text2)
#WC: создайте переменную "number" со значением 89, без кавычек

#UC: посмотрите что возвращает функция внизу
##print(number)
#UC: также можно комбинировать числа и текст
##print(text+str(number)+" "+text2)
#UC: тоже можно делать и через {}
##print("{}{} {}".format(text,number,text2))
#WC: это выдаст ошибку, чтобы исправить ошибку окружите переменную "number" str()
#чтобы получилось str(number)
#WC: заполните три строчки внизу, чтобы получить Имя Фамилия
## name = ""
## lastName = ""
##

# UC: Можно выполнять различные манипуляции с текстом например убрать cимволы
##nameWithSpaces = "   something   "
##print( nameWithSpaces )
# UC: Cтрочка внизу убирает все пробелы
##print( nameWithSpaces.strip())
# UC: Cтрочка внизу убирает все символы "А"
print( "ABRACADABRA".strip("A") )
# UC: Вы можете также убирать так же элементы справа или слева
##print( "    TEXT".rstrip() )
##print( "......TEXT.....".rstrip('.'))
##print( "    TEXT".lstrip() )
##print( "......TEXT.....".lstrip('.'))
#WC: напишите команду которую уберёт все "<" из примера
##strangeText = "<<<<TEXT<<<<<"#code should go here
##print( strangeText )

#UC: также важно уметь заменять значения
##text = "This is instructor's code"
#UC: Строчки внизу заменяет
##newText = text.replace("instructor","student")
##print( newText )
#UC: Можно использовать переменные
##std = "student"
##print( text.replace("instructor",std) )
#WC: Cоздайте переменную со своим именем и замените "instructor" на ваше имя.





