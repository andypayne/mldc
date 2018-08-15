import xgboost as xgb
import pandas as pd
boston_data = pd.read_csv("boston_data.csv")
X, y = boston_data.iloc[:,:-1], boston_data.iloc[:,-1]
boston_dmatrix = xgb.DMatrix(data=X, label=y)
params = {"objective": "reg:linear", "max_depth": 4}
l1_params = [1, 10, 100]
rmses_l1 = []

for reg in l1_params:
  params["alpha"] = reg
  cv_results = xgb.cv(dtrain=boston_dmatrix, params=params, nfold=4, num_boost_round=10, metrics="rmse", as_pandas=True, seed=123)
  rmses_l1.append(cv_results["test-rmse-mean"].tail(1).values[0])

print("Best RMSE as a function of L1:")
# zip([1,2,3],["a","b""c"]) = [1,"a"],[2,"b"],[3,"c"]
# list() is needed to cast/instantiate the generator output of zip (python 3) as a list
print(pd.DataFrame(list(zip(l1_params, rmses_l1)), columns=["l1", "rmse"]))

