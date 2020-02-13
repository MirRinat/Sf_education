import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn import metrics
import pickle
import seaborn as sb



df = pd.read_excel("../data/dzRF.xlsx")
# print(df)


#Исследования данных
n_samples, n_features = df.shape
print("Количество наблюдений ",n_samples)
print("Количество атрибутов ", n_features)


# noshow: 0 если клиент явился по записи, 1 – если нет (значение, которое нам предстоит предсказать)
#
# book_tod: время дня, на которое записан клиент (утро, день или вечер)
# book_dow: день недели, на который записан клиент
# book_category: тип услуги (стрижка или окраска), на которую записан клиент
# book_staff: имя парикмахера, к которому записан клиент
# last_category: тип услуги, на которую клиент приходил в прошлый раз
# last_staff: имя парикмахера, который обслуживал клиента в прошлый визит
# last_day_services: количество услуг, оказанных клиенту в прошлый визит
# last_receipt_tot: сумма, заплаченная клиентом в прошлый визит
# last_dow: день недели предыдущей записи
# last_tod: время дня предыдущей записи
# last_noshow: явился ли клиент в прошлый раз
# last_prod_flag: купил ли клиент какой-либо продукт в прошлый визит
# last_cumrev: общий доход, который клиент принес парикмахерской
# last_cumbook: сколько всего раз данный клиент записывался в парикмахерскую
# last_cumstyle: сколько раз клиент был записан на стрижку
# last_cumcolor: сколько раз клиент был записан на окраску
# last_cumprod: сколько раз клиент что-то покупал
# last_cumcancel: сколько раз клиент отменял запись заранее
# last_cumnoshow: сколько раз клиент отменял запись в последний момент или просто не являлся
# recency: сколько дней прошло с последней записи


# print(df.head(5))
pd.set_option('display.max_columns',None)#показывает усеченный вид
# print(df.head(5))
description = df.describe()
description.to_excel('../data/description.xlsx')
# print(description)

print("Количество пустых значений")
print(df.isnull().sum())
#все пустые значения категориальные,когда заменим их на фиктивнеы,у недостающих будет значение 0 во всех столбцах

print("Количество атрибутов {}  и наблюдений {} до замены категориальных на фиктивные".format(df.shape[1],df.shape[0]))
# замена на фиктивные(но не обязательно)
df = pd.get_dummies(df)
# print(df)
print("Количество атрибутов {}  и наблюдений {} после замены категориальных на фиктивные".format(df.shape[1],df.shape[0]))
print("Количество пустых значений после замены категориальных на фиктивные")
# print(df.isnull().sum())

#Описание таблицы после очистки
description_after_preprocessing = df.describe().to_excel('../data/description_after_preprocessing.xlsx')


#cколько процентов не явились и явились?
# df['noshow'].value_counts().plot(kind='bar')
# plt.title("Неявки")

print("%f процентов не явились по записи " %(df.noshow[df.noshow == 1].count()/df.noshow.count() * 100))

#есть ли корелляция между атрибутами
corr = df.corr()
corr.to_excel("../data/correlation.xlsx")

#корреляция
triangle = corr.abs().where(np.tril(np.ones(corr.shape), k=-1).astype(np.bool))
print("Самая сильная корреляция")
print(triangle.stack().sort_values(ascending=False)[:10])


#удалить кореляционные атрибуты
to_drop = ['last_cumstyle','last_cumbook','book_category_STYLE']
df.drop(to_drop,axis=1)
print("Количество атрибутов после удаления сильно скоррелированных атрибутов:", df.shape)

#разделим атрибуты на x и y, где x-это все атрибуты,а у-это,что нам нужно предсказать(noshow)

y = df.noshow
X = df.drop('noshow',axis=1)

#разбиваем выборку на учебную и тестовую
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, stratify=y)
#где stratify=y обеспечивает равномерное распределение 11% неявок в тестовую и учебную выборку


#подбираем оптимальные параметры

#создание классификатора
clf = RandomForestClassifier(random_state=47,n_jobs=-1,n_estimators=200,class_weight='balanced_subsample')
#random_state=47 - количество попыток
#n_jobs=-1 - количество ядер "-1" - задействует вся ядра
#n_estimators - количество деревьев

#Выбор гиперпараметров: пробуем max_features от 1 до кол-ва атрибутов и max_depth от 5 до 30:
param_destributions = {'max_features': list(range(1,X.shape[1])), "max_depth": list(range(5,30))}


#обучаем модель
#Проверим, насколько хорошо классификатор работает без настройки гиперпараметров:
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Результат на тестовых данных(модель по умолчанию): %f " % (100*metrics.balanced_accuracy_score(y_test,y_pred)))

#теперь проверим с гиперпараметрами
#Пробуем 50 разных сочетаний гиперпараметров, тестируем каждое сочетание 5 раз (перекрёстная проверка),
# оцениваем по количеству правильно классифицированных наблюдений в обоих классах:
# random_search = RandomizedSearchCV(clf,param_distributions=param_destributions,n_iter=50,cv=5,scoring="balanced_accuracy",n_jobs=-1)
# random_search.fit(X_train,y_train)

# #Сохраняем оптимальную модель и смотрим на ее параметры:
# model = random_search.best_estimator_
# print("Оптимальные параметры: %s , оценка гиперпараметров: %0.2f " % (random_search.best_params_, random_search.best_score_))
#ограничение параметра max_depth позволяет избежать переобучения, и потому дает лучшие результаты)

#сохраним обученную модель

filename = "my_model_RF.sav"
# pickle.dump(model,open(filename,'wb'))

#после записи в файл,можно  его загрузить
model = pickle.load(open(filename, 'rb'))

#Оценить, насколько хорошо модель предсказывает случаи неявки и поздней отмены записи

# #Предсказание класса на тестовых данных:
y_pred = model.predict(X_test)
#balanced_accuracy_score = (процент правильно предсказанных явок + процент правильно предсказанных неявок)/2
print("Результат на тестовых данных: %f " %(100*metrics.balanced_accuracy_score(y_test,y_pred)))

#Посмотрим на конкретное количество наблюдений, записанных классификатором в тот или иной класс, для этого посчитаем матрицу неточностей:
cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
print("Матрица неточностей:")
print(cnf_matrix)

sb.heatmap(cnf_matrix, annot=True, cmap='Blues', fmt='g', xticklabels=["явка","неявка"], yticklabels=["явка","неявка"])
plt.ylabel('Реальное значение')
plt.xlabel('Предсказанное значение')
plt.show()
