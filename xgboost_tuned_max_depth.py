housing_dmatrix = xgb.DMatrix(data=X,label=y)

params = {"objective":"reg:linear"}

max_depths = [2, 5, 10, 20]
best_rmse = []

for curr_val in max_depths:
  params["max_depth"] = curr_val
  cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=2, num_boost_round=10, early_stopping_rounds=5, metrics="rmse", as_pandas=True, seed=123)
  best_rmse.append(cv_results["test-rmse-mean"].tail().values[-1])

print(pd.DataFrame(list(zip(max_depths, best_rmse)),columns=["max_depth","best_rmse"]))


