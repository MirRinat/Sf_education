import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.model_selection import train_test_split
import scipy as sp
from sklearn.svm import SVC
import pickle
from sklearn.model_selection import RandomizedSearchCV
from sklearn import metrics


# загрузим данные и посмотрим на них
df = pd.read_excel("../data/svm_course_travel_insurance_data.xlsx")
pd.set_option('display.max_columns', None)
print(df.head())


print("Статистика по данным:")
description = df.describe(include='all')
print(description)
description.to_excel("../data/data_description.xlsx")

print("Количество пустых значений:")
print(df.isnull().sum())

# почистим данные:
# Duration (длительность путешествия) не может быть 0 и вряд ли может быть несколько тысяч (учитывая средние значения)
print("%f процентов значений Duration = 0" % ((df.Duration[df.Duration==0].count()/df.Duration.count())*100))

df = df[df.Duration > 0]

# plt.hist(df.Duration, bins=range(min(df.Duration), max(df.Duration) + 100, 100))
# plt.show()

print("%f процентов значений Duration > 500" % ((df.Duration[df.Duration>500].count()/df.Duration.count())*100))
df = df[df.Duration <= 500]

# # Gender (пол): слишком много значений отсутствует
df = df.drop('Gender',axis=1)

# # Age (возраст застрахованного): 118-летний путешественник выглядит подозрительно
# plt.hist(df['Age'], bins=range(min(df['Age']), max(df['Age']) + 1, 1))
# plt.show()

df = df[df.Age < 100]

print("Чистые данные:")
print(df.describe(include='all'))

print("Количество пустых значений:")
print(df.isnull().sum())

# Claim: какой процент застрахованных воспользовались страховкой?
# df['Claim'].value_counts().plot(kind='bar')
# plt.title("Claim")
# plt.show()
print("%f процентов застрахованных воспользовались страховкой" %((df.Claim[df.Claim=='Yes'].count()/df.Claim.count())*100))

# # нормализация численных атрибутов
numeric_features = df.select_dtypes(include=[np.number])
print("Численные атрибуты: ", numeric_features.columns.values)
print("До нормализации:")
print(numeric_features.describe())

numeric_features_scaled =(numeric_features-numeric_features.min())/(numeric_features.max()-numeric_features.min())
print("После нормализации:")
print(numeric_features_scaled.describe())

df[numeric_features.columns.values] = numeric_features_scaled[numeric_features.columns.values]

print("Чистые и нормализованные данные:")
print(df.describe(include='all'))

# # разделим данные на X (все атрибуты) и y (колонка Claim: то, что надо предсказать)
y = df.Claim.eq('Yes').astype(int)
X = df.drop('Claim',axis=1)

# # заменим категориальные атрибуты на фиктивные переменные (0 и 1 для каждого значения)
X.head().to_excel("../data/head_before_dummies.xlsx")
X = pd.get_dummies(X,drop_first=True)
X.head().to_excel("../data/head_after_dummies.xlsx")
print("Количество наблюдений и атрибутов после замены категориальных переменных на фиктивные:", X.shape)

# # корреляция между атрибутами
corr = X.corr()
corr.to_excel("../data/correlations.xlsx")

# нижний треугольник матрицы
triangle = corr.abs().where(np.tril(np.ones(corr.shape), k=-1).astype(np.bool))

print("Самая сильная корреляция:")
print(triangle.stack().sort_values(ascending=False)[:10])

# уберем лишние столбцы
to_drop = [column for column in triangle.columns if any(triangle[column] > 0.8)]
print("Убираем столбцы: ", to_drop)
X = X.drop(to_drop, axis=1)

print("Количество наблюдений и атрибутов после удаления сильно скоррелированных атрибутов:", X.shape)

preprocessed_description = X.describe(include='all')
preprocessed_description.to_excel("../data/preprocessed_data_description.xlsx")

# # теперь можем приступать к обучению классификатора
#
# # разделим данные на две части: 30% отложим для тестирования
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,stratify=y)
#
clf = SVC(class_weight='balanced',kernel="rbf")
#
param_distributions = {"C": sp.stats.uniform(0.5, 4000), "gamma": sp.stats.uniform(0.001, 1)}
# random_search = RandomizedSearchCV(clf, param_distributions=param_distributions, n_iter=45, cv=5, scoring="balanced_accuracy", n_jobs=-1)
# random_search.fit(X_train, y_train)
# model = random_search.best_estimator_
# print("Оптимальные параметры: %s, оценка на учебных данных: %0.2f" % (random_search.best_params_, random_search.best_score_))
#
# # сохраним обученную модель
filename = 'svc_model.sav'
#pickle.dump(model, open(filename, 'wb'))
#
model = pickle.load(open(filename,'rb'))
#
y_pred = model.predict(X_test)
#
print("Результат на тестовых данных: %f" % (100*metrics.balanced_accuracy_score(y_test, y_pred)))
#
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
#
print("Матрица неточностей:")
print(cnf_matrix)
sb.heatmap(cnf_matrix, annot=True, cmap='Blues', fmt='g')
plt.ylabel('Реальное значение Claim')
plt.xlabel('Предсказанное значение Claim')
plt.show()


