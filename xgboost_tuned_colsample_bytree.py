
# Tuning colsample_bytree
# In scikit-learn's RandomForestClassifier or RandomForestRegressor this was
# called max_features. In both xgboost and sklearn, this parameter (although
# named differently) simply specifies the fraction of features to choose
# from at every split in a given tree. In xgboost, colsample_bytree must be
# specified as a float between 0 and 1.

housing_dmatrix = xgb.DMatrix(data=X,label=y)
params={"objective":"reg:linear","max_depth":3}
colsample_bytree_vals = [0.1, 0.5, 0.8, 1]
best_rmse = []

# Vary the hyperparameter value 
for curr_val in colsample_bytree_vals:
  params["colsample_bytree"] = curr_val
  cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=2, num_boost_round=10, early_stopping_rounds=5, metrics="rmse", as_pandas=True, seed=123)
  best_rmse.append(cv_results["test-rmse-mean"].tail().values[-1])

print(pd.DataFrame(list(zip(colsample_bytree_vals, best_rmse)), columns=["colsample_bytree","best_rmse"]))


