import metrics as metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
import pickle
import scipy as sp
import seaborn as sb


df = pd.read_csv("../data/dzSVM.csv")

# print(df.head())

###########Иследование данных#############
n_samples, n_features = df.shape
print("Количество артибутов", n_features)
print("Количество наблюдений ", n_samples)

pd.set_option('display.max_columns',None)
# print(df.head())

print("Статистика по данным:")
# print(df.describe(include='all'))
describe = df.describe(include='all')
describe.to_excel("../data/describe.xlsx")

# plt.hist(df[~np.isnan(df['CLAGE'])]['CLAGE'])
# plt.show()

countClageMore700 = df.CLAGE[df.CLAGE >= 700].count()
print("%f процентов значений CLAGE >= 700 (кредит старше 58 лет), всего %i наблюдений" % ((countClageMore700/df.CLAGE.count())*100, countClageMore700))
#убираем выбросы
df.drop(df[df.CLAGE >= 700].index, inplace=True)

# print("Количество пустых значений\n", df.isnull().sum())

#заполним пустые значения медианным значением
df.fillna(df.median(), inplace=True)

#количество пустых значений после очистки
# print(df.isnull().sum())

df.fillna(df.mode().iloc[0],inplace=True)

# print("Количество пустых значений после заполнения категориальных переменных:")
# print(df.isnull().sum())

#сохранение данных после очистки
df.to_excel('../data/afterClean.xlsx')
#
# print("Чистые данные:")
# print(df.describe(include='all'))

#Проверка насколько сбалансированы
# df['BAD'].value_counts().plot(kind='bar')
# plt.title("BAD")
# plt.show()

print("%f процентов заемщиков не выплатили кредит" %((df.BAD[df.BAD==1].count()/df.BAD.count()) * 100))


#######НОРМАЛИЗАЦИЯ ДАННЫХ##########

#численные атрибуты
numeric_features = df.select_dtypes(include=[np.number])
# print("Численные атрибуты\n",numeric_features.columns.values)

#до нормализации
# print("до нормалицзации\n",numeric_features.describe())

#после нормализации
numeric_features_scaled = (numeric_features - numeric_features.min())/(numeric_features.max() - numeric_features.min())
# print("после нормализации\n", numeric_features_scaled.describe())

#добавим нормализованные численные атрибуты к другим данным
df[numeric_features.columns.values] = numeric_features_scaled[numeric_features.columns.values]
# print("Чистые и нормализованные данные\n",df.describe(include='all'))

#замена катеригиональных JOB, Reason в фиктивные
df = pd.get_dummies(df,drop_first=True)
# print("Первые пять наблюдений после замены категориальных переменных на фиктивные")
# print(df.head())
#
# print("Количество наблюдений и атрибутов после замены категориальных переменных на фиктивные:", df.shape)
#
# print("Чистые и нормализованные данные с фиктивными переменными вместо категориальных:")
# print(df.describe(include='all'))

#Проверим, есть ли корреляция между атрибутами. Сохраним корреляционную матрицу в Excel-файле:
corr = df.corr()
corr.to_excel('../data/correlations.xlsx')

#посмотреть самые большие кореляции
triangle = corr.abs().where(np.tril(np.ones(corr.shape),k=-1).astype(np.bool))
print("Самая сильная корелляция")
print(triangle.stack().sort_values(ascending=False)[:7])

#######разделение данных на учебную и тестовую выборку#######

#разделим данные на Х атрибуты и у класс(то,что нужно предсказать)
y = df.BAD
X = df.drop('BAD',axis=1)

#Теперь разделим данные на две части, на 70% данных будем обучать модель, 30% отложим для тестирования:

#параметр stratify гарантирует, что пропорции классов (20% невыплат) будут одинаковыми в тестовой и в учебной выборках)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,stratify=y)

###########Подобрать оптимальные гиперпараметры#############

#создание классификатора
cfl = SVC(class_weight='balanced',kernel='rbf')

#выбор гиперпараметров
param_distributions = {'C': sp.stats.uniform(0.5,500),'gamma':sp.stats.uniform(0.01,1)}

######обучение модели
# random_search = RandomizedSearchCV(cfl,param_distributions=param_distributions,n_iter=40,scoring="balanced_accuracy",n_jobs=-1)
# random_search.fit(X,y)

#сохраним модель и смотрим параметры
# model = random_search.best_estimator_
# print("Оптимальные параметры: %s, оценка на учебных данных: %0.2f" % (random_search.best_params_, random_search.best_score_))
filename = 'svc_model.sav'
# pickle.dump(model, open(filename, 'wb'))
model = pickle.load(open(filename,'rb'))

#предсказание класса на тестовых данных
y_pred = model.predict(X_test)
print("Результат на тестовых данных: %f" % (100*metrics.balanced_accuracy_score(y_test, y_pred)))

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Матрица неточностей:")
print(cnf_matrix)

sb.heatmap(cnf_matrix, annot=True, cmap='Blues', fmt='g', xticklabels=["выплата","невыплата"], yticklabels=["выплата","невыплата"])
plt.ylabel('Реальное значение')
plt.xlabel('Предсказанное значение')
plt.show()





