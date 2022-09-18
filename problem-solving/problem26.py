t=int(input())
for i in range(t):
    m=int(input())
    s=input()
    str=[]
    for k in range(m):
        if(s[k]=='A'):
            str.append('T')
        elif(s[k]=='T'):
            str.append('A')
        elif(s[k]=='C'):
            str.append('G')
        elif(s[k]=='G'):
            str.append('C')
    
    print("".join(str))
        