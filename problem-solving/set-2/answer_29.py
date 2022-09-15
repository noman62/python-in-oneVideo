# SQUARE ROOT FACTORIAL
import math

x = math.factorial(4)
y = math.factorial(x)
print("Factorial of 4: ", x)
print("Factorial of(4!): ", y)
for i in range(5):
    y = int(math.sqrt(y))

print("The integer result: ", y)
