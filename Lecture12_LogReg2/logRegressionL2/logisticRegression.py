import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
import sklearn.metrics


def printOutTheCoefficients(params,coeffecients,intercept):
    tParams = params[np.newaxis].T
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams,tCoeffs],axis=1)
    totalDF = pd.DataFrame(data=total)
    totalDF.to_excel("modelOutput.xlsx")
    print(totalDF)

columnWIV = ["recoveries",
             "creditScore",
             "int_rate",
             "total_rec_late_fee",
             "term",
             "annual_inc",
             "revol_util",
             "creditPurpose",
             "dti",
             "inq_last_6mths",
             "default_ind"]

df = pd.read_csv("Data/150K.csv",skipinitialspace=True, usecols= columnWIV)

df["revol_util"].fillna(100,inplace=True)

purpose = pd.get_dummies(df['creditPurpose'])#создание фиктивных переменных
df.drop('creditPurpose', axis=1,inplace=True)

dfReady = pd.concat([df,purpose],axis=1)

dfResults = dfReady['default_ind']
dfInputs = dfReady.drop('default_ind',axis=1)

X_train, X_test,y_train, y_test = train_test_split(dfInputs,dfResults,test_size=0.3, random_state=1)

LogReg = LogisticRegression()
LogReg.fit(X_train,y_train)

y_pred = LogReg.predict(X_test)

printOutTheCoefficients(dfInputs.columns.values,LogReg.coef_,LogReg.intercept_)