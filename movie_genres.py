import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = ...
y = df['Sci-Fi']

X_train, X_test, y_train, y_test = train_test_split(df['plot'], y, test_size=0.33, random_state=53)
count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train.values)  # create bow vectors
count_test = count_vectorizer.transform(X_test.values)  # create bow vectors for the test data using the dictionary fitted above

