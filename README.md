
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


## Pipeline workflow

- Reliable way to go from raw data to trained model
- Each step is a tuple with two elements
  - Name: string
  - Transform: obj implementing .fit() and .transform()


## Interaction terms

Interaction terms describe mathematically when tokens appear together.

"English teacher for 2nd grade"
vs
"2nd grade - budget for English teacher"

```
x1 = presence of term 1
x2 = presence of term 2

a * x1 + b * x2 + c * (x1 * x2)
```

An interaction term is an added expression for the coexistence of term 1 and term 2, with its own weight (c here). So the presence of both terms can be weighted as more significant than either individual term.


## Hashing trick

Useful for dimensionality reduction, to reduce memory usage, etc. Replace text terms by their hashes.


# ML-Based Dialogue Systems

- NLU
- Dialogue state manager
- API logic - connected to a DB, API, etc
- Natural language response generator


## Classification

### Binary

Metric for binary classification models - AUC of ROC curve
Area under the curve of the Receiver Operating Characteristic curve
x axis = FP rate
y axis = TP rate
Higher area = higher TP rate, lower FP rate
= greater probability that a randomly chosen positive data point will have a higher rank than a randomly chosen negative data point

### Multiclass

Metric for multiclass - accuracy score and confusion matrix
Accuracy = (tp + tn) / (tp + tn + fp + fn)
Confusion matrix - rows are actual values, columns are predicted values

## Preprocessing for supervised learning

- Numeric features should be scaled (Z-scored)
- Categorical features should be encoded (one-hot)


## Regression

### Common metrics

- Root mean squared error (RMSE)
- Mean absolute error (MSE)


## XGBoost

Base learners are combined as an ensemble meta-model. When combined, the final prediction is nonlinear.


### When to use

- Large number of training samples - > 1000 training samples and < 100 features
  - # features < # training samples
- Mixture of categorical and numeric features, or only numeric features

### When not to use

- Not ideal for image recognition, computer vision, NLP/NLU
- # of training samples is significantly smaller than # of features

### Common loss functions in xgboost

- `reg:linear` - regression
- `reg:logistic` - classification problems when only a decision is desired, with no probability
- `binary:logistic` - probability rather than just decision

### Regularization

Regularization can be a control on model complexity, by penalizing models that are more complex.

Regularization parameters in XGBoost:

- gamma - min loss reduction allowed for a split to occur
- alpha - L1 regularization on leaf weights, larger values = more regularization
- lambda - L2 regularization on leaf weights

### Tuning xgboost

Common tree tunable parameters:

- learning rate/eta - how quickly the model fits the residual error using additional base learners - lower requires more boosting rounds to achieve the same error
- gamma - min loss reduction to crate a new tree split
- alpha - L1 regularization on leaf weights
- lambda - L2 regularization on leaf weights
- max_depth - max depth per tree
- subsample - % of samples used per tree - low -> underfitting problems, high -> overfitting
- colsample_bytree - % of features used per tree - additional regularization

Common linear tunable parameters:

- alpha - L1 regularization on weights
- lambda - L2 regularization on weights
- lambda_bias - L2 regularization on bias

The number of boosting rounds is also a tunable parameter on both tree-based and linear-based ensembles.


