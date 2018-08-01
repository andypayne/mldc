import xgboost as xgb
import pandas as pd

class_data = pd.read_csv("classification_data.csv")

# Convert data to a dmatrix
churn_dmatrix = xgb.DMatrix(data=churn_data.iloc[:,:-1], label=churn_data.month_5_still_here)

# Parameter dictionary for XGBoost
params = {"objective": "binary:logistic", "max_depth": 4}

# Cross validation object
# - nfold = how many folds (k)
# - num_boost_round = number of trees
cv_results = xgb.cv(dtrain=churn_dmatrix, params=params, nfold=4, num_boost_round=10, metrics="error", as_pandas=True)

print("Accuracy = %f" % ((1 - cv_results["test-error-mean"]).iloc[-1]))




churn_dmatrix = xgb.DMatrix(data=X, label=y)
params = {"objective":"reg:logistic", "max_depth":3}
cv_results = xgb.cv(dtrain=churn_dmatrix, params=params, nfold=3, num_boost_round=5, metrics="error", as_pandas=True, seed=123)

print(cv_results)
# Print the accuracy
print(((1-cv_results["test-error-mean"]).iloc[-1]))



# Perform cross_validation
cv_results = xgb.cv(dtrain=churn_dmatrix, params=params, nfold=3, num_boost_round=5, metrics="auc", as_pandas=True, seed=123)

print(cv_results)
# Print the AUC (area under the curve)
print((cv_results["test-auc-mean"]).iloc[-1])


