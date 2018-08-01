from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
dt_clf_4 = DecisionTreeClassifier(max_depth=4)
dt_clf_4.fit(X_train, y_train)
y_pred_4 = dt_clf_4.predict(X_test)

accuracy = float(np.sum(y_pred_4==y_test))/y_test.shape[0]
print("accuracy:", accuracy)

