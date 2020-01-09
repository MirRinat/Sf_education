#!/usr/bin/python
# -*- coding: utf-8 -*-

def doSimpleCalculations():
    #  создайте переменную равную 99999
    a = 99999
    #  создайте переменную равную 11111
    b = 11111
    return(a/b)#  верните поделите первую переменную на вторую


def combineStringsSimple():
  #  создайте переменную Societe
  a = "Societe "
  #  создайте переменную Financiers'
  b = "Financiers "
  #  cоздайте переменную Rules
  c = "Rules"
  return (a + b + c)#   верните Societe Financiers Rule


def combineNumsStrings():
  #  создайте переменную равную 9000
  a = 9000
  #  создайте переменную Societe Financiers rules over
  b = 'Societe Financiers rules over '
  #  создайте переменную  times
  c = ' times'
  return (b + str(a) + c)#  скомбинируйте все перменные чтобы получить Societe Finacnciers rules over 9000 times

print(combineStringsSimple())

def combineStringsNums():
  #  1.создайте ТЕКСТОВУЮ переменную равную '9000'
  a = "9000"
  #  2.создайте ЧИСЛОВУЮ переменную 500
  b = 500
  return (int(a) / b)#поделите ПРЕОБРАЗОВАННУЮ ТЕКСТОВУЮ переменную(1.) на ЧИСЛОВУЮ(2.)
print(combineStringsNums("3000"))