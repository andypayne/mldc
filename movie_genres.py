import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = ...
y = df['Sci-Fi']

X_train, X_test, y_train, y_test = train_test_split(df['plot'], y, test_size=0.33, random_state=53)
count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train.values)  # create bow vectors
count_test = count_vectorizer.transform(X_test.values)  # create bow vectors for the test data using the dictionary fitted above

# Multinomial Naive Bayes works well with CountVectorizer because it takes
# integer inputs.
# Multinomial Naive Bayes may not work as well with floats like TF-IDF
# weighted inputs. Instead try Support Vector Machines or Linear Models.
# But you can try this first.
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

nb_classifier = MultinomialNB()
nb_classifier.fit(count_train, y_train)
pred = nb_classifier.predict(count_test)
metrics.accuracy_score(y_test, pred)
# => 0.8584...
metrics.confusion_matrix(y_test, pred, labels=[0,1])
# => array([[6140,  563],
#           [ 864, 2242]])
#            Predicted
# Actual    Action  Sci-Fi
# Action      6140    563
# Sci-Fi       864   2242


