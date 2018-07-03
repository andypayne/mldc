
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


