# Greater Average
# Problem Code:AVGPROBLEM

n=int(input())

i=0
while(i<n):
    a,b,c=map(int,input().split())
    s1=float((a+b)/2)
    if(s1>c):
        print("YES\n")
    else:
        print("NO\n")
   
    i+=1