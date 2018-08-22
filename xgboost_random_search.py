import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.model_selection import RandomizedSearchCV

housing_data = pd.read_csv("ames_housing_trimmed_processed.csv")
X,y = housing_data[housing_data.columns.tolist()[:-1]], housing_data[housing_data.columns.tolist()[-1]]
housing_dmatrix = xgb.DMatrix(data=X, label=y)
gbm_param_grid = {
  'learning_rate': np.arange(0.05, 1.05, 0.05),
  'n_estimators':  0[200],
  'subsample':     np.arange(0.05, 1.05, 0.05)
}

gbm = xgb.XGBRegressor()
randomized_mse = RandomizedSearchCV(estimator=gbm, param_distributions=gbm_param_grid, n_iter=25, scoring='neg_mean_squared_error', cv=4, verbose=1)
randomized_mse.fit(X, y)

print("Best parameters found: ",randomized_mse.best_params_)
# Best parameters found: {'subsample': 0.60000000000000009, 'n_estimators': 200, 'learning_rate': 0.20000000000000001}
print("Lowest RMSE found: ", np.sqrt(np.abs(randomized_mse.best_score_)))
# Lowest RMSE found: 28300.2374291






gbm_param_grid = {
    'n_estimators': [25],
    'max_depth': range(2, 12)
}

gbm = xgb.XGBRegressor(n_estimators=10)
randomized_mse = RandomizedSearchCV(estimator=gbm, param_distributions=gbm_param_grid, n_iter=5, scoring="neg_mean_squared_error", cv=4, verbose=1)
randomized_mse.fit(X, y)

print("Best parameters found: ", randomized_mse.best_params_)
print("Lowest RMSE found: ", np.sqrt(np.abs(randomized_mse.best_score_)))

# Fitting 4 folds for each of 5 candidates, totalling 20 fits
# Best parameters found:  {'max_depth': 6, 'n_estimators': 25}
# Lowest RMSE found:  36909.98213965752
