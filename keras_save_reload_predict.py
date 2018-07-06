from keras.models import load_model

model.save('model_file.h5')
my_model = load_model('model_file.h5')
predictions = my_model.predict(data_to_predict_with)
probability_true = predictions[:,1]  # Extract second column with numpy indexing
print(my_model.summary())

