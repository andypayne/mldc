import pandas as pd
import xgboost as xgb
import numpy as np

housing_data = pd.read_csv("ames_housing_trimmed_processed.csv")
X, y = housing_data[housing_data.columns.tolist()[:-1]], housing_data[housing_data.columns.tolist()[-1]],
housing_dmatrix = xgb.DMatrix(data=X, label=y)

tuned_params = {"objective": "reg:linear", "colsample_bytree": 0.3, "learning_rate": 0.1, "max_depth": 5}

tuned_cv_results_rmse = xgb.cv(dtrain=housing_dmatrix, params=tuned_params, nfold=4, num_boost_round=200, metrics="rmse", as_pandas=True, seed=123)

print("Tuned rmse: %f", % ((tuned_cv_results_rmse["test-rmse-mean"]).tail(1)))





# Tuning the number of boosting rounds

housing_dmatrix = xgb.DMatrix(data=X, label=y)
params = {"objective":"reg:linear", "max_depth":3}
num_rounds = [5, 10, 15]
final_rmse_per_round = []

for curr_num_rounds in num_rounds:
  cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=3, num_boost_round=curr_num_rounds, metrics="rmse", as_pandas=True, seed=123)
  final_rmse_per_round.append(cv_results["test-rmse-mean"].tail().values[-1])

num_rounds_rmses = list(zip(num_rounds, final_rmse_per_round))
print(pd.DataFrame(num_rounds_rmses,columns=["num_boosting_rounds","rmse"]))



# With early stopping

housing_dmatrix = xgb.DMatrix(data=X, label=y)
params = {"objective":"reg:linear", "max_depth":4}
cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=3, num_boost_round=50, early_stopping_rounds=10, metrics="rmse", as_pandas=True, seed=123)
print(cv_results)


