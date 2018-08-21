import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.model_selection import GridSearchCV

housing_data = pd.read_csv('ames_housing_trimmed_processed.csv')
X, y = housing_data[housing_data.columns.tolist()[:-1]], housing_data[housing_data.columns.tolist()[-1]
housing_dmatrix = xgb.DMatrix(data=X,label=y)
# 4 x 1 x 3 = 12 combinations, so 12 models will be trained
gbm_param_grid = { 'learning_rate': [0.01, 0.1, 0.5, 0.9], 'n_estimators': [200], 'subsample': [0.3, 0.5, 0.9] }

gbm = xgb.XGBRegressor()
grid_mse = GridSearchCV(estimator=gbm, param_grid=gbm_param_grid, scoring='neg_mean_squared_error', cv=4, verbose=1)
grid_mse.fit(X, y)

print("Best parameters found: ",grid_mse.best_params_)
# Best parameters found: {'learning_rate': 0.1, 'n_estimators': 200, 'subsample': 0.5}

print("Lowest RMSE found: ", np.sqrt(np.abs(grid_mse.best_score_)))
# Lowest RMSE found:  28530.1829341

