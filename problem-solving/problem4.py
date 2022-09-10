n=int(input())
i=0
while(i<n):
    a,b,c=map(int,input().split())
    
    if(a<=b and c<=b):
         print("Yes\n")
    else:
        print("No\n")
    
    i+=1