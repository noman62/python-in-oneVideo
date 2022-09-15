import numpy as np
from numpy import *

input = np.array([[0 ,1 ,2 ,3, 4, 5, 6, 7],
                  [9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ],
                  [0 ,9 ,1, 8, 2, 7, 3, 6],
                  [4 ,5 ,6 ,3 ,2 ,7 ,0 ,9],
                  [3 ,8 ,2, 7,  0, 5, 9, 4],
                  [1, 6 ,4 ,8 ,3 ,9 ,2 ,5],
                  [2  ,0 ,4 ,9 ,5, 8, 6, 7],
                  [ 0 ,5 ,1 ,6 ,2 ,7 ,3 ,8]])
target = np.array([[-1 ,-1],
                   [1 , 1],
                   [-1,1],
                   [1,-1],
                   [1,1],
                   [1,-1],
                   [-1,1],
                   [-1,-1]])

print('Dimension ',input.ndim)
def sigmoid(X):
    return 1 / (1 + np.exp(-X))


def sigmoid_derivative(x):
    return x * (1 - x)

np.random.seed(1)
print("Input = ", input)
Vi=2*np.random.random((8,3))-1
Wi=2*np.random.random((3,2))-1
print('Initial weights1 = ', Vi)
print('Initial weights2 = ', Wi)
alpha = 10e-6


n=40000
for i in range(n):
    hiddenoutput = sigmoid(np.dot(input, Vi))
    output = sigmoid(np.dot(hiddenoutput, Wi))
    Yi_error = target - output

    # error1=np.dot(error2,w2.T)*hiddenoutput*(1-hiddenoutput)
    Yi_delta = Yi_error * sigmoid_derivative(output)
    Zi_error = np.dot(Yi_delta, Wi.T)
    Zi_delta = Zi_error * sigmoid_derivative(hiddenoutput)
    Wi += alpha* np.dot(hiddenoutput.T, Yi_delta)
    Vi += alpha*np.dot(input.T, Zi_delta)

output = sigmoid(np.dot(hiddenoutput, Wi))

print('No of epochs ',n)
print('Final weights1 = ', Vi)
print('Final weights2 = ', Wi)

print('Output')
print(output)