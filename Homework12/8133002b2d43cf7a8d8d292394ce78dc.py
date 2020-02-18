import pandas_datareader as wb
import pandas as pd
from datetime import datetime
from sklearn import linear_model
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#В этом упражнении вы узнаете влияют ли разницы в ставках в различных валютах на курсы этих валют.
#Скачайте "Overnight London Interbank Offered Rate (LIBOR), based on U.S. Dollar " с Jan 1 2010 до сегодня с сайта FRED

#Скачайте "Overnight London Interbank Offered Rate (LIBOR), based on Euro  " с Jan 1 2010 до сегодня с сайта FRED
#Скачайте "U.S. / Euro Foreign Exchange Rate"  с Jan 1 2010 до сегодня с сайта FRED
#Уберите NaN значения из каждой dataframe, используя df.dropna()
#Объедините их вместе для создания общих дат
#Посчитайте АБСОЛЮТНУЮ разницу между ставками EUR и USD 
#Посчитайте разницу в ПРОЦЕНТАХ как для изменения в EUR FX ставки и разницу в ставках EUR и USD
#Сделайте линейную регрессию, чтобы выяснить связь между ставками EUR и USD и изменения EUR FX
#Проверьте свой r2 показатель
#Ответьте на вопрос -- влияют ли изменения в ставках на изменение на курсы валют?





