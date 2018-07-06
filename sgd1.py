import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD

predictors = np.loadtxt('...', delimiter=',')
n_cols = predictors.shape[1]  # Need the number of columns in the input

def get_new_model(input_shape = input_shape):
  model = Sequential()
  model.add(Dense(100, activation='relu', input_shape=input_shape))
  model.add(Dense(100, activation='relu')
  model.add(Dense(1))
  return model

lr_to_test = [0.000001, 0.01, 1]
for lr in lr_to_test:
  model = get_new_model(input_shape=[n_cols,])
  my_optimizer = SGD(lr=lr)
  model.compile(optimizer=my_optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
  model.fit(predictors, target, validation_split=0.3)  # Using split validation (alternative to k-fold cross validation)
  



