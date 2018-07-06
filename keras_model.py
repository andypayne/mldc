import numpy as np
from keras.layers import Dense
from keras.models import Sequential

predictors = np.loadtxt('predictors_data.csv', delimiter=',')
n_cols = predictors.shape[1]  # Need the number of columns in the input
model = Sequential()  # In sequential models, each layer has inpputs only to the layer immediately after it
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))  # Add layer 1, 100 nodes, input can have any number of data points
model.add(Dense(100, activation='relu')  # Add layer 2
model.add(Dense(1))  # Add layer 3
model.compile(optimizer='adam', loss='mean_squared_error')  # Compile
model.fit(predictors, target)  # Fit


