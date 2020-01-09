#import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import quandl

###GETTING DATA####
magnit = pd.read_csv('Data/MGNT_191201_200101.csv')
magnit.set_index('<DATE>',inplace=True)
magnit.to_excel('recData/MGNT_from_csv_index.xlsx')