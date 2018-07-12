from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

X_train, X_test, y_train, y_test = train_test_split(sample_df[['text']], pd.get_dummies(sample_df['label']), random_state=2)

# setup pl ...
pl = Pipeline([
       ('vec', CountVectorizer()),
       ('clf', OneVsRestClassifier(LogisticRegression()))
     ])

pl.fit(X_train, y_train)
# => Pipeline(steps=[('clf', OneVsRestClassifier(LogisticRegression()))], ...)

accuracy = pl.score(X_test, y_test)
print('accuracy on numeric data: ', accuracy)


