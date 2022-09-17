# li=[1,2,3,4,5,6]
# final=list(map(lambda x:x*2,li))
# print(final)3=
import numpy as np
# n3=np.zeros((10,3))
# print(n3)
n1=np.array([10,20])
n2=np.array([40,50])
sum=np.intersect1d(n1,n2)
sum1=np.sum([n1,n2],axis=0)


print(sum1)
