from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import FeatureUnion

X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing', 'text']], pd.get_dummies(sample_df['label']), random_state=2)

get_text_data = FunctionTransformer(lambda x: x['text'], validate=False)
get_numeric_data = FunctionTransformer(lambda x: x[['numeric', 'with_missing']], validate=False)

numeric_pipeline = Pipeline([
                     ('selector', get_numeric_data),
                     ('imputer', Imputer())
                   ])
text_pipeline = Pipeline([
                  ('selector', get_text_data),
                  ('vectorizer', CountVectorizer())
                ])


#union = FeatureUnion([
#          ('numeric', numeric_pipeline),
#          ('text', text_pipeline)
#        ])


pl = Pipeline([
       ('union', FeatureUnion([
                   ('numeric', numeric_pipeline),
                   ('text', text_pipeline)
                 ])),
       ('clf', OneVsRestClassifier(LogisticRegression()))
     ])

pl.fit(X_train, y_train)

accuracy = pl.score(X_test, y_test)
print('accuracy on all data: ', accuracy)


