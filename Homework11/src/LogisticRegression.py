import pandas as pd
import numpy as np
#в этом упражнении мы создадим простейшую логистическую модель, которая
#будет определять вероятность того, что определенный человек зарабатывает больше 80к долларов
#на основе социэкономических характеристик

# from WOE import data_vars, char_bin, momo_bin
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
import sklearn.metrics

from WOE import data_vars


def printOutTheCoefficients(params,coeffecients,intercept):
    tParams = params[np.newaxis].T
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams,tCoeffs],axis=1)
    totalDF = pd.DataFrame(data=total)
    totalDF.to_excel("modelOutput.xlsx")
    print(totalDF)

#загрузите данные из файла

df = pd.read_csv('../data/adultIncome_proc.csv')

#уберите очевидно(без вычислений) скорелированные параметры
to_drop = ['Unnamed: 0']
df = df.drop(to_drop,axis=1)

#сгрупируйте Marital Status до 4 категорий -- Married, Separated, Never Married, Widowed
df['Martial-status'].replace(' Married-civ-spouse', 'Married',inplace=True)
df['Martial-status'].replace(' Divorced', 'Separated',inplace=True)
df['Martial-status'].replace(' Married-spouse-absent', 'Widowed',inplace=True)
# print(df)

#сгрупируйте страны до двух: рожденные в США и нет
df['Native Country'] = df['Native Country'].eq(' United-States').astype(int)

#вычислите и определите если какие-то параметры скореллированы с друг другом и избавьтесь от одного из них
corr = df.corr()
corr.to_excel('../data/correlation.xlsx')
#найдите и уберите статистически незначительные или неправдоподобные параметры используя WOE file
iv_df,iv = data_vars(df,df['making above 80K'])
iv.to_excel('../data/Iv.xlsx')

#dummy encode все не количественные элементы

#уберите все неколичественные элементы которые вы заменили на dummy variables
to_ebc= ['Martial-status', 'Race', 'Sex','Native Country', 'type-of-employment', 'occupation','Degree']
varia = pd.get_dummies(df[to_ebc])
df.drop(to_ebc,axis=1, inplace=True)
df = pd.concat([df,varia],axis=1)
print(df)
#создайте таблицу в которой только КОЛИЧЕСТВЕННЫЕ значения -- начальные и dummy
num_df = pd.get_dummies(df)
num_df.to_excel('../data/num_df.xlsx')
#разделите на сэт результатов и входных параметров -- 80k+ и входные параметры
y = num_df['making above 80K']
X = num_df.drop('making above 80K',axis=1)
#сделайте разделение на трейнинговый и тестовый сет
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7,stratify=y)
#запустите логистическую регрессию
clf = LogisticRegression()
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
# print("Результат на тестовых данных: %f " % (100*sklearn.metrics.balanced_accuracy_score(y_test,y_pred)))
#сохраните результат используя функцию printOutCoefficients в excel и прогоните 5 людей(строк из файла)
print(confusion_matrix(y_test,y_pred))
printOutTheCoefficients(X.columns.values, clf.coef_, clf.intercept_)
# через вашу модель и интерпретируйте результат
y_finish = clf.predict(X.head(5))
print(y_finish)
