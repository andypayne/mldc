
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

names = ["crime","zone","industry","charles", "no","rooms","age", "distance", "radial","tax","pupil","aam","lower","med_price"]
data = pd.read_csv("boston_housing.csv",names=names)
X, y = data.iloc[:,:-1], data.iloc[:,-1]

rf_pipeline = Pipeline[("st_scaler", StandardScaler()), ("rf_model",RandomForestRegressor())]

scores = cross_val_score(rf_pipeline,X,y, scoring="neg_mean_squared_error",cv=10)
# abs to switch the neg MSE above to a pos
final_avg_rmse = np.mean(np.sqrt(np.abs(scores)))
print("Final RMSE:", final_avg_rmse)
# Final RMSE: 4.54530686529

