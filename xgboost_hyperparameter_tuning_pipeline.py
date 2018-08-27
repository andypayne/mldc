import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV

names = ["crime","zone","industry","charles","no", "rooms","age", "distance","radial","tax", "pupil","aam","lower","med_price"]
data = pd.read_csv("boston_housing.csv",names=names)
X, y = data.iloc[:,:-1],data.iloc[:,-1]
# xgb_pipeline = Pipeline[("st_scaler", StandardScaler()), ("xgb_model",xgb.XGBRegressor())]
xgb_pipeline = Pipeline([("st_scaler", StandardScaler()), ("xgb_model",xgb.XGBRegressor())])
# Naming scheme: <name of step>__<name of hyperparameter>
gbm_param_grid = {
    'xgb_model__subsample': np.arange(0.05, 1, 0.05),
    'xgb_model__max_depth': np.arange(3, 20, 1),
    'xgb_model__colsample_bytree': np.arange(0.1, 1.05, 0.05)
}

randomized_neg_mse = RandomizedSearchCV(estimator=xgb_pipeline, param_distributions=gbm_param_grid, n_iter=10, scoring='neg_mean_squared_error', cv=4)
randomized_neg_mse.fit(X, y)

print("Best rmse: ", np.sqrt(np.abs(randomized_neg_mse.best_score_)))
# Best rmse: 3.9966784203040677

print("Best model: ", randomized_neg_mse.best_estimator_)
# Best model:  Pipeline(steps=[('st_scaler', StandardScaler(copy=True, with_mean=True, with_std=True)),
# ('xgb_model', XGBRegressor(base_score=0.5, colsample_bylevel=1,
#        colsample_bytree=0.95000000000000029, gamma=0, learning_rate=0.1,
#        max_delta_step=0, max_depth=8, min_child_weight=1, missing=None,
#        n_estimators=100, nthread=-1, objective='reg:linear', reg_alpha=0,
#        reg_lambda=1, scale_pos_weight=1, seed=0, silent=True,
#        subsample=0.90000000000000013))])




# parameter grid
gbm_param_grid = {
    'clf__learning_rate': np.arange(0.05, 1, 0.05),
    'clf__max_depth': np.arange(3, 10, 1),
    'clf__n_estimators': np.arange(50, 200, 50)
}

randomized_roc_auc = RandomizedSearchCV(estimator=pipeline, param_distributions=gbm_param_grid, n_iter=2, scoring="roc_auc", cv=2, verbose=1)
randomized_roc_auc.fit(X, y)

print(randomized_roc_auc.best_score_)
print(randomized_roc_auc.best_estimator_)
"""
Fitting 2 folds for each of 2 candidates, totalling 4 fits
0.9975999999999999
Pipeline(memory=None,
     steps=[('featureunion', FeatureUnion(n_jobs=1,
       transformer_list=[('num_mapper', DataFrameMapper(default=False, df_out=True,
        features=[(['age'], Imputer(axis=0, copy=True, missing_values='NaN', strategy='median', verbose=0)), (['bp'], Imputer(axis=0, copy=True, missing_values='NaN', st...
       reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
       silent=True, subsample=1))])
"""

