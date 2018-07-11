
## Activation Functions

- Originally tanh [sigmoid or logistic sigmoid?]
- Now usually Rectified Linear Activation Unit (ReLU)  ```__/```
  - RELU(x) = 0 if x < 0, x if x >= 0


## Error Measurement - Loss Functions

### Mean Squared Error (MSE)

MSE = avg(error^2)

### Gradient Descent

Minimize MSE

1. Imagine you're in a dark field and you want to find the lowest point, but all you can see is the next step
2. Feel the ground around to determine the slope
3. Take a small step (learning rate) in the direction of the steepest downward slope
4. Repeat until every direction is uphill (positive slope)

#### GD Slope

To calc the slope for a weight, multiply:

1. Slope of the loss function with respect to the value at the node we feed into
2. The value of the node that feeds into our weight
3. Slope of the activation function with respect to the value we feed into

Slepe of the mean squared loss function with respect to prediction = 2 * (predicted value - actual value) = 2 * error


## Categorical data

Pandas has the 'category' data type to encode categorical data numerically.

```cat_data = some_data.astype('category')```

To see the underlying  values:

```python
dummies = pd.get_dummies(cat_data[['label']], prefix_sep='_')  # Also called a binary indicator representation
```


## Loss

The spam problem - if only 1% of email is spam, then a classifier that always returned 'not spam' would be 99% accurate.

So log loss is used, and focus is on minimizing loss, vs maximizing accuracy. It factors in the probability or confidence that a classification is correct. It's better to be less confident than confident and wrong, because confident (high p) classifications are penalized.


## Train/Test Splitting

The standard train-test split won't work well in some situations, for example when in a classification problem the data set has at least one class with a small number of instances. The split might result in all of the instances being in the test data, and the model won't be able to determine classes it's never seen.

So _StratifiedShuffleSplit_ can be used. However, it only works with a single target variable.


## Bag of words in Scikit-learn

CountVectorizer() - tokenizes strings, builds a vocabulary, counts the occurrences of each token in the vocabulary



