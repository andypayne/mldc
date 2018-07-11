
data_to_train = df[NUMERIC_COLUMNS].fillna(-1000)  # Subset to only numeric columns, then fill NAs with -1000 (to differentiate from zeroes)
labels_to_use = pd.get_dummies(df[LABELS])  # Produce binary indicators for the target categories
# multilabel_train_test_split is implemented here:  https://github.com/drivendataorg/box-plots-sklearn/blob/master/src/data/multilabel.py
X_train, X_test, y_train, y_test = multilabel_train_test_split(data_to_train, labels_to_use, size=0.2, seed=123)

from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# OneVsRestClassifier lets you treat each column of y independently, by fitting a separate classifier to each column
clf = OneVsRestClassifier(LogisticRegression())
clf.fit(X_train, y_train)
print("Accuracy = {}".format(clf.score(X_test, y_test)))



