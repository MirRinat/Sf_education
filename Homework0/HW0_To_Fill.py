def doSimpleCalculations():
    #  создайте переменную 99999
    a = 99999
    #  создайте переменную 11111
    b = 11111
    return int(a/b)#  верните первую переменную, поделенную на вторую
#print(doSimpleCalculations())

def combineStringsSimple():
  #  создайте переменную SF
  a = "SF"
  #  создайте переменную Education
  b = " Education "
  #  создайте переменную Rules
  c = "Rules"
  return (a+b+c)#   составьте из трех переменных выше фразу "SF Education Rules"
#print(combineStringsSimple())

def combineNumsStrings():
  #  создайте переменную 5000
  a = "5000 "
  #  создайте переменную SF Education обучил более
  b = "SF Education обучил более "
  #  создайте переменную студентов
  c = "студентов"

  return (b+a+c)#  составьте из трех переменных выше фразу "SF Education обучил более 5000 студентов"
# print(combineNumsStrings() == "SF Education обучил более 5000 студентов")
# print(combineNumsStrings())
# print("SF Education обучил более 5000 студентов")

#создайте функцию convertStringToNum, у которой будет один входной параметр
#возьмите этот параметр, преобразите его в число и поделите его на 50
#верните результат
def convertStringToNum(a):
    return int(float(a) / 50)

#print(convertStringToNum(2500))
