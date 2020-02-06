import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.model_selection import train_test_split
import scipy as sp
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn import metrics
from matplotlib.legend_handler import HandlerLine2D
from src.plotting_func import plot_2d_separator, plot_tree_partition
from sklearn.tree import export_graphviz
import graphviz


# загрузим данные и посмотрим на них
df = pd.read_excel("../data/telecom_churn.xlsx")
print("Количество наблюдений: ", df.shape[0])
print("Количество атрибутов: ", df.shape[1])

pd.set_option('display.max_columns', None)

print(df.head())


# статистика по данным
description = df.describe(include='all')
description.to_excel("../data/data_description.xlsx")

print("Количество пустых значений:")
print(df.isnull().sum())

# Churn: сколько клиентов ушло?
# df['Churn'].value_counts().plot(kind='bar')
# plt.title("Churn")
# plt.show()

print("%f процентов клиентов ушли" %((df.Churn[df.Churn=='Yes'].count()/df.Churn.count())*100))


y = df.Churn.eq('Yes').astype(int)
X = df.drop('Churn', axis=1)

# tenure == 0: новые клиенты
print("Количество новых клиентов: ", X.tenure[X.tenure==0].count())

print("TotalCharges, новые клиенты:")
print(X.TotalCharges[X.tenure==0])

X.TotalCharges = X.TotalCharges.fillna(value=0.0)

print("Количество пустых значений:")
print(X.isnull().sum())

# # многие атрибуты нерелевантны для тех, у кого не подключен интернет
# # создадим новый стобец hasInternetService
# # и два новых бинарных стобца: hasFiber и hasDSL
#
X = X.assign(hasInternetService = X.InternetService.ne('No').astype(int))
X = X.assign(hasFiber = X.InternetService.eq('Fiber optic').astype(int))
X = X.assign(hasDSL = X.InternetService.eq('DSL').astype(int))

X.drop('InternetService', axis=1, inplace=True) # столбец InternetService теперь не нужен


# преобразуем бинарные переменные в 0 и 1

X.gender = X.gender.eq('Male').astype(int)

yesOrNoVariableColumns = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling']

for c in yesOrNoVariableColumns:
    X[c] = X[c].eq('Yes').astype(int)


# оставшиеся категориальные переменные преобразуем в фиктивные переменные

X = pd.get_dummies(X,drop_first=True)
print("Количество наблюдений и атрибутов после замены категориальных переменных на фиктивные:", X.shape)


# корреляция между атрибутами
corr = X.corr()
corr.to_excel("../data/correlations.xlsx")

# нижний треугольник матрицы
triangle = corr.abs().where(np.tril(np.ones(corr.shape), k=-1).astype(np.bool))

print("Самая сильная корреляция:")
print(triangle.stack().sort_values(ascending=False)[:10])

# уберем лишние столбцы
to_drop = ['tenure', 'hasDSL', 'MonthlyCharges']
print("Убираем столбцы: ", to_drop)
X = X.drop(to_drop, axis=1)

print("Количество наблюдений и атрибутов после удаления сильно скоррелированных атрибутов:", X.shape)

# статистика по данным после обработки
description_after_preprocessing = X.describe(include='all')
description_after_preprocessing.to_excel("../data/data_description_after_preprocessing.xlsx")


# теперь можем приступать к обучению классификатора

# разделим данные на две части: 30% отложим для тестирования
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,stratify=y, random_state=47)

clf = RandomForestClassifier(random_state=47, n_jobs=-1, n_estimators=100, class_weight='balanced_subsample')

filename = 'rf_model.sav'

# clf.fit(X_train,y_train)
# y_pred = clf.predict(X_test)

# print("Результат на тестовых данных (модель по умолчанию): %f" % (100*metrics.balanced_accuracy_score(y_test, y_pred)))


# param_distributions = {"max_features": list(range(1,X.shape[1])), "max_depth": list(range(3, 30))}
#
# randomized_search = RandomizedSearchCV(clf, param_distributions=param_distributions, n_iter=60, cv=5, scoring="balanced_accuracy", n_jobs=-1, random_state=47)
# randomized_search.fit(X_train, y_train)
# model = randomized_search.best_estimator_
# print("Оптимальные параметры: %s, оценка на учебных данных: %0.2f" % (randomized_search.best_params_, randomized_search.best_score_))
#
# # сохраним обученную модель
# pickle.dump(model, open(filename, 'wb'))



model = pickle.load(open(filename, 'rb'))
y_pred = model.predict(X_test)

print("Результат на тестовых данных: %f" % (100*metrics.balanced_accuracy_score(y_test, y_pred)))

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
#
# print("Матрица неточностей:")
# print(cnf_matrix)
#
# sb.heatmap(cnf_matrix, annot=True, cmap='Blues', fmt='g')
# plt.ylabel('Реальное значение Churn')
# plt.xlabel('Предсказанное значение Churn')
# plt.show()


# информативность (важность) атрибутов

# n_features = X.shape[1]
# plt.barh(range(n_features), model.feature_importances_)
# plt.yticks(np.arange(n_features), X.columns.values.tolist())
# plt.xlabel("Важность атрибута")
# plt.tight_layout()
# plt.show()

tree = model.estimators_[0]

export_graphviz(tree, out_file="../data/first_tree.dot", class_names=["No churn", "Churn"], feature_names = X.columns.values.tolist(), impurity=False)

with open("../data/first_tree.dot") as f:
    tree_graph = f.read()

graphviz.Source(tree_graph, filename="../data/tree", format='png').view()
