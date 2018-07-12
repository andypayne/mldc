from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

pl = Pipeline([
       ('clf', OneVsRestClassifier(LogisticRegression()))
     ])

