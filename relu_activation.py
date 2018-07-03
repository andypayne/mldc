import numpy as np

def relu(input):
    return max(0, input)


print(relu(3))
print(relu(-3))

