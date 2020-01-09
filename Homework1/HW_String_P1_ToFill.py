# Заполните инструкции внизу
# Если вы видите в консоле "Process finished with exit code 0"
# запустите правильный файл _Test

#Fill in the exercises below per instructions
#If you see  "Process finished with exit code 0"
# in console please run the right file

#create the function named "exampleOne" that will return "I am alive! Alive!".
#создайте функцию с именем "exampleOne"  которая вернёт "I am alive! Alive!"
#cделайте это до того как запустить тестовый файл
def exampleOne():
    return "I am alive! Alive!"


#cоздайте функцию с именем exampleTwo, у которой будет один входной параметер.
#возьмите этот параметер и добавьте "And this alive too: " перед ним перед тем как 
#вернуть
def exampleTwo(a):
    return "And this alive too: " + a


#cоздайте функцию с именем exampleThree, у которой будет три входных параметра.
#верните их одним текстовым элементом разделенными тремя точками ...
#пример атлична...атлична...например
def exampleThree(a,b,c):
    q = "..."
    return str(a)+q+str(b)+q+str(c)


#cоздайте функцию с именем exampleFour, у которой будут два входных параметра.
#первый параметр будет текст над которым нужно работать, второй текст который убрать
#Пример:
#первый парам: %%%%ХАХА%%%%, второй %, результат ХАXА
def exampleFour(a,b):
    return a.strip(b)




#более сложный:
#cоздайте функцию с именем exampleFive, у которой будет один входной параметер.
#преобразите его таким образом, чтобы из него исчезли все вопросительные знаки
#пример: ????Why am i doing? this???? => Why am i doing this
def exampleFive(a):
    return a.replace('?','')
# print(exampleFive("????Why am i doing? this????"))


#более сложный:
#cоздайте функцию с именем exampleSix, у которой будет один входной параметер.
#перед возвращением замените все "ss" на "s" и "tt" на "t"
def exampleSix(a):
   b = a.replace('ss', 's')
   c = b.replace("tt", "t")
   return c
#print(exampleSix("Lett'ss ssee if itt workss"))




