import numpy as np
# sigmoid function


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_derivative(x):
    return x*(1-x)


# input dataset
x = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

# target output
t = np.array([[0], [1], [1], [0]])
np.random.seed(1)

# initialize weights randomly
vi = 2*np.random.random((3, 4))-1
wi = 2*np.random.random((4, 1))-1
print("Initialize weights between input layer and hidden layer : ")
print(vi)
print("Initialize weights between Hidden layer and output layer : ")
print(wi)

for j in range(60000):
    zi = sigmoid(np.dot(x, vi))
    yi = sigmoid(np.dot(zi, wi))
    yi_error = t-yi

yi_delta = yi_error*sigmoid_derivative(yi)
zi_error = yi_delta.dot(wi.T)
zi_delta = zi_error*sigmoid_derivative(zi)
wi += zi.T.dot(yi_delta)
vi += x.T.dot(zi_delta)

# output
print("Output after training")
yi = sigmoid(np.dot(zi, wi))
outputs = yi
print(outputs)

# output for new situation
zi = sigmoid(np.dot(([1, 0, 0]), vi))
yi = sigmoid(np.dot(zi, wi))
output = yi
print('output for a new situation [1,0,0]')
print(output)
