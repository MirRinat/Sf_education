def combineStringNumsSmart():
  #  создайте переменную равную 185
  a = '185'
  #  оздайте переменную равную Data Science Academy
  b = 'Data Science Academy'
  #  создайте переменную равную В чате хххх на данный момент ХХХ студентов
  c = 'В чате xxxx на данный момент XXX студентов'
  c = c.replace('xxxx',b)
  c = c.replace('XXX',a)
  return (c)#  скомбинируйте все перменные чтобы получить В чате Data Science Academy на данный момент 185 студентов



#  arrays
def simpleArrayString():
  #  создайте переменную равную "The population of the Roman Empire was XX million at 25BC"
  a = "The population of the Roman Empire was XX million at 25BC"
  #  создайте массив с элементами 125.5, 56.8, 12.1
  b = [125.5, 56.8, 12.1]
  a = a.replace("XX", str(b[1]))
  return (a)# скомбинируйте все перменные чтобы получить "The population of the Roman Empire was 56.8 million at 25BC"
#print(simpleArrayString())
# arrays2
def addingArrayString():
  #  создайте переменную равную "The population of the Roman Empire was XX million at 25BC"
  a = "The population of the Roman Empire was XX million at 25BC"
  #  создайте пустой массив
  b = []
  #  добавьте  12.1
  b.append(12.1)
  #  добавьте  18.1
  b.append(18.1)
  #  добавьте  56.8
  b.append(56.8)
  return (a.replace('XX',str(b[2]))) # скомбинируйте все перменные чтобы получить "The population of the Roman Empire was 56.8 million at 25BC" "The population of the Roman Empire was 56.8 million at 25BC"
#print(addingArrayString())

  #  arrays3
def measuringLengthofArray():
  #  создайте переменную равную "Квинтилий Вар потерял XX легионов в Германии: XXX, XXX, и XXX"
  a = "Квинтилий Вар потерял XX легионов в Германии: XXX, XXX, и XXX"
  #  создайте массив с элементами  Legio XVII, Legio XVIII and Legio XIX
  b = ['Legio XVII', 'Legio XVIII', 'Legio XIX']
  c = a.replace('XX','3')
  c = c.replace('3X','{}')
  c = c.replace('легионов', 'легиона')
  return (c.format(b[2],b[0],b[1]))# скомбинируйте все перменные чтобы получить "Квинтилий Вар потерял 3 легиона в Германии: Legio XIX, Legio XVII, и Legio XVIII"
#print(measuringLengthofArray())
#  iteration
def doIterations():
  #  создайте массив с элементами BSC, LEH, WB
  a = ['BSC', 'LEH', 'WB']
  #  создайте переменную равную \n XXX обанкротился
  b = '\n XXX обанкротился'
  #  создайте пустую текстовую переменную, которая будет использована для финального результата
  c = ''
  #  для каждого элемента в массиве
  #  добавьте "\n %ЭЛЕМЕНТ% обанкротился" к тому, что уже есть в финальной текстовой переменной
  for i in a:
      c += b
      c = c.replace('XXX',i)
  #  напечатайте финальную переменную
  return (c)#верните финальный результат, чтобы он выглядел как \n BSC обанкротился\n LEH обанкротился\n WB обанкротился
#print(doIterations())

def doRangeIteration():
  #  создайте пустой массив
  a = []
  #  для каждого числа от 1 до 1000
  for i in range(1,1000):
      a.append(i)
  #  добавьте его к начальному массиву
#  print(a.index(566), len(a))

  return (a)#  верните массив
#print(doRangeIteration())
def doDictionary():
    # создайте словарь со следующими парами ключ-значение Нерва-98, Траян-117, Адриан-138
    dict = {'Нерва': 98,'Траян':117, 'Адриан':138}
    # создайте переменную равную Траян
    a = 'Траян'
    # создайте переменную XXXXX умер в XXX г н.э.
    c = 'XXXXX умер в XXX г н.э.'
    c = c.replace('XXXXX','{}')
    c = c.replace('XXX','{}')
    return (c.format(a,dict[a]))#использую только переменные наверху верните Траян умер в 117 г н.э.
#print(doDictionary())
def myFirstFunction(key,value):
    #  создайте переменную \nXXXXX умер в XXX г н.э.
    a = '\nXXXXX умер в XXX г н.э.'
    a = a.replace('XXXXX','{}')
    a = a.replace('XXX','{}')
    return (a.format(key,str(value))) #верните заформативрованные текст используя параметры как  as in \n Адриан умер в 138 г н.э.
#print(myFirstFunction('Адриан',138))
def doFunctionCalling():
    #  создайте словарь со следующими парами ключ-значение Нерва-98, Траян-117, Адриан-138
    dict = {'Нерва': 98,'Траян':117, 'Адриан':138}
    #  создайте пустую текстовую переменную, которая будет использована для финального результата
    a = ''
    #  для каждой комбинации ключ-значение
    #  добавьте результат функции уже к имеющемуся результату
    for key in dict:
        a += '\n ' + key + ' умер в ' + str(dict[key]) + ' г н.э.'
    return(a) #верните финальный результат в форме \n Нерва умер в 98 г н.э.\n Траян умер в 117 г н.э.\n Адриан умер в 138 г н.э.
#print(doFunctionCalling())



