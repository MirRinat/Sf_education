#!/usr/bin/python
# -*- coding: utf-8 -*-

import WorkSimple as work

over9000 = "Societe Financiers rules over 9000 times"
simpleCount = 0

if(work.combineStringsSimple() == "Societe Financiers Rules"):
    print("\nТест на операции с текстом успешен")
    simpleCount += 1

if(work.doSimpleCalculations() == 9 ):
    print("\nТест на арифметику успешен")
    simpleCount += 1

if(work.combineNumsStrings() == over9000):
    print("\nТест на преобразование числа в текст успешен")
    simpleCount += 1

if (work.combineStringsNums() == 18):
    print("\nТест на преобразование текста в число успешен")
    simpleCount += 1

print("\nВсего {} из 4 простых заданий выполнены".format(simpleCount))