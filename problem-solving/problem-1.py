import math   
a,b,c= map(int,input().split())
s1=math.floor(c//3*b)
s2=c%3*a
# print(s1)
sum=s1+s2
if(sum<c*a):
    print(sum)
else:
    print(c*a)