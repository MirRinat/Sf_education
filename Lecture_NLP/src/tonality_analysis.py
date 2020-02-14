import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from spacy.lang.ru import RussianLemmatizer
import pymystem3
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


comments = pd.read_excel('../data/market_comments.xlsx')
print(comments.columns)
print(comments.comment.count())
print("Отрицательные отзывы ", comments[comments.tonality == 'negative'].comment.count())
print("Положительные отзывы ", comments[comments.tonality == 'positive'].comment.count())

toy_corpus = comments.comment[:3]
# print(toy_corpus)
# vect = CountVectorizer()
# vect.fit(toy_corpus)

# print("РАзмер словаря", len(vect.vocabulary_))
# print("Словарь ", vect.vocabulary_)
#
# bag_of_words = vect.transform(toy_corpus)
# print(bag_of_words.toarray())

text_train, text_test, y_train, y_test = train_test_split(comments.comment, comments.tonality, stratify=comments.tonality)

vect = CountVectorizer().fit(text_train)
X = vect.transform(text_train)
# print(repr(X))

features_names = vect.get_feature_names()
print("Количество атрибутов", len(features_names))
print("Первые 20 ", features_names[:20])
print("Последние 20", features_names[-20:])

model = LogisticRegression()

model.fit(X, y_train)

X_test = vect.transform(text_test)
print(model.score(X_test,y_test))

nltk.download("punkt")

stemmer = nltk.stem.SnowballStemmer("russian")
print([stemmer.stem(word) for word in word_tokenize(comments.comment[7].lower())])


def stemming(doc):
    tokens = [stemmer.stem(word) for word in word_tokenize(doc.lower())]
    return " ".join(tokens)

# text_train = [stemming(doc) for doc in text_train]
# text_test = [stemming(doc) for doc in text_test]
#
# vect = CountVectorizer().fit(text_train)
# X_train = vect.transform(text_train)
#
# features_names = vect.get_feature_names()
# print("Количество атрибутов", len(features_names))
# print("Первые 20 ", features_names[:20])
# print("Последние 20", features_names[-20:])


nltk.download('stopwords')
stop = stopwords.words('russian')

# print("Пеовые 10 стопслов", stop[:10])

# vect = CountVectorizer(min_df=3, stop_words=stop).fit(text_train)
# X_train = vect.transform(text_train)
#
# model = LogisticRegression()
# model.fit(X_train,y_train)
#
#
# X_test = vect.transform(text_test)
# print(model.score(X_test,y_test))


#######TF-idf
# vect = TfidfVectorizer().fit(text_train)
# X_train = vect.transform(text_train)
#
# model = LogisticRegression()
# model.fit(X_train,y_train)
#
#
# X_test = vect.transform(text_test)
# print(model.score(X_test,y_test))
#
# max_value = X_train.max(axis=0).toarray().ravel()
# sorted_by_tfidf = max_value.argsort()
#
# features_names = np.array(vect.get_feature_names())
#
# print("Максимальный TF IDF", features_names[sorted_by_tfidf[:20]])
# print("Минимальный TF IDF", features_names[sorted_by_tfidf[-20:]])
#
# sorted_by_idf = np.argsort(vect.idf_)
# print("Минимальный IDF", features_names[sorted_by_tfidf[:20]])

vect = CountVectorizer(ngram_range=(1,2)).fit(toy_corpus)
print("Словарь ", vect.get_feature_names())

