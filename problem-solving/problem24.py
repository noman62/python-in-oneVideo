# from traceback import print_tb


# n=int(input())
# for i in range(n):
#     a=int(input())
#     if(a<=50):
#         print("LEFT\n")
#     else:
#         print("RIGHT\n")
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=x*3

plt.plot(x,y)
plt.show()