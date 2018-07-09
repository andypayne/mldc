import numpy as np

def compute_log_loss(predicted, actual, eps=1e-14):
  """ Compute the log loss between predicted and actual 1D arrays
      :param predicted: The predicted probabilities, floats 0-1
      :param actual: The actual binary labels, either 0 or 1
      :param eps (optional): used to offset predicted values to get around log(0) = infinity
  """
  predicted = np.clip(predicted, eps, 1 - eps)  # Adjust predicted to be in the range (eps, 1 - eps)
  loss = -1 * np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))
  return loss




