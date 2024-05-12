# raw text -> tokenization -> text -> cleaning -> pos tagging -> stopwords -> lemmetization -> clean -> ML model
import os
import pandas as pd
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

nltk.download('all')

os.chdir('..')
data = pd.read_csv('resources/training.csv')

print(data.head())

sentences = data['text']
y = data['label']

sentences_train, sentences_test, y_train, y_test = train_test_split(
   sentences, y, test_size=0.25, random_state=100)


vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)




#assign corpus to data['text']

