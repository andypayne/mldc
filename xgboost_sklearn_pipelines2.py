from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline

X.LotFrontage = X.LotFrontage.fillna(0)
steps = [("ohe_onestep", DictVectorizer(sparse=False)),
         ("xgb_model", xgb.XGBRegressor())]
xgb_pipeline = Pipeline(steps)
xgb_pipeline.fit(X.to_dict("records"),y)

