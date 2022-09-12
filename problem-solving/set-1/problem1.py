# vector
# list=[1,2,3,3]
# print(list)
# using numpy
# Importing numpy  
# import numpy as k  
# creating list  
# list1 = [10, 20, 30, 40, 50]  
# # Creating 1-D Horizontal Array  
# vtr = k.array(list1)  
    
  
# print("We create a vector from a list:")  
# print(vtr)  
# matrix
# x=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# y=[[5,8,1],
#  [6,7,3],
#  [4,5,9]]
# result=[[0,0,0],
# [0,0,0],
# [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j]+y[i][j]

# for r in result:
#     print(r)
# Array
import array as arr
a=arr.array('i',[1,2,3])

print ("Array before insertion : ", end =" ")
for i in range(len(a)):
    print(a[i],end=" ")

print()
 
# inserting array using
# insert() function
a.insert(3, 4)
 
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()