import numpy as np

training_inputs=np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

training_outputs=np.array([[0],
                           [1],
                           [1],
                           [0]])

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

np.random.seed(1)

synaptic_weights=2*np.random.random((3,1))-1

print('\nRandom Initial synaptic weights: ')
print(synaptic_weights)

n=int(input("enter the number of iteration "))

for iteration in range(n):
    input_layer=training_inputs
    outputs=sigmoid(np.dot(input_layer,synaptic_weights))
    error=training_outputs-outputs
    adjustments=error*sigmoid_derivative(outputs)
    synaptic_weights=synaptic_weights+np.dot(input_layer.T, adjustments)

print("\nthe number of iteration: " + str(n))
print("\n weights after training : ")
print(synaptic_weights)
print("\noutputs after training: ")
print(outputs)