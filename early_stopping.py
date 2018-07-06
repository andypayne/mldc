from keras.callbacks import EarlyStopping

...

early_stopping_monitor = EarlyStopping(patience=2)  # patience = # of epochs of no improvement before stopping
model.fit(predictors, target, validation_split=0.3, epochs=20, callbacks=[early_stopping_monitor])  # Default # of epochs Keras trains is 10

