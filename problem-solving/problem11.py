n=int(input())

i=0
while(i<n):
    a=int(input())
    if(a<100):
        print(a,"\n")
    elif(a>100 and a<=1000):
        print(a-25,"\n")
    elif(a>1000 and a<=5000):
        print(a-100,"\n")
    elif(a>5000):
        print(a-500,"\n")
    i+=1