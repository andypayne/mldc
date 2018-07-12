from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric']], pd.get_dummies(sample_df['label']), random_state=2)

# setup pl ...
pl = Pipeline([
       ('clf', OneVsRestClassifier(LogisticRegression()))
     ])

pl.fit(X_train, y_train)
# => Pipeline(steps=[('clf', OneVsRestClassifier(LogisticRegression()))], ...)

accuracy = pl.score(X_test, y_test)
print('accuracy on numeric data, no nans: ', accuracy)


X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing']], pd.get_dummies(sample_df['label']), random_state=2)
pl.fit(X_train, y_train)
# => ValueError when adding 'with_missing'


from sklearn.preprocessing import Imputer

pl = Pipeline([
       ('imp', Imputer()),  # Imputer fills in the NaN values with the mean of the column
       ('clf', OneVsRestClassifier(LogisticRegression()))
     ])

pl.fit(X_train, y_train)
# => Pipeline(steps=[('clf', OneVsRestClassifier(LogisticRegression()))], ...)

accuracy = pl.score(X_test, y_test)
print('accuracy on numeric data, with nans: ', accuracy)



