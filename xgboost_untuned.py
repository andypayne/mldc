import pandas as pd
import xgboost as xgb
import numpy as np

housing_data = pd.read_csv("ames_housing_trimmed_processed.csv")
X, y = housing_data[housing_data.columns.tolist()[:-1]], housing_data[housing_data.columns.tolist()[-1]],
housing_dmatrix = xgb.DMatrix(data=X, label=y)

untuned_params = {"objective": "reg:linear"}

untuned_cv_results_rmse = xgb.cv(dtrain=housing_dmatrix, params=untuned_params, nfold=4, metrics="rmse", as_pandas=True, seed=123)

print("Untuned rmse: %f", % ((untuned_cv_results_rmse["test-rmse-mean"]).tail(1)))


