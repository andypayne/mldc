import pandas as pd
from keras.utils import to_categorical
data = pd.read('basketball_shot_log.csv')  # This could be done with Pandas or Numpy
predictors = data.drop(['shot_result'], axis=1).as_matrix()
target = to_categorical(data.shot_result)  # One hot encoding of shot_result
n_cols = predictors.shape[1]  # Need the number of columns in the input
model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))  # 2 here should really be the number of distinct values in shot_result
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(predictors, target)
