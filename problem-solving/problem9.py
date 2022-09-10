import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

training_inputs=np.array([[0,0,1],
[1,1,1],
[1,0,1],
[0,1,1]
])

def __sigmoid(self,x):
    return 1/(1+exp(-x))
training_outputs=np.array([[0,1,1,0]])

np.random.seed(1)

synaptic_weights=2*np.random.random((3,1))-1

print("\nRandom initial synaptic Weights:",)
print(synaptic_weights)

for iteration in range(1):
    input_layer=training_inputs
    outputs=sigmoid(np.dot(input_layer,synaptic_weights))

print("\nOutputs after training:")
print(outputs)

outputs=sigmoid(np.dot([1,0,0],synaptic_weights))

print("\nOutput for new situation:")
print(outputs)