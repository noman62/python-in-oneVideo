n = int(input())

i = 0
while (i < n):
    a, b, c, d = map(int, input().split())
    if (a >= b):
        if (c >= d):
            print(a+c, "\n")
        else:
            print(a+d, "\n")
    else:
         if(c >= d):
            print(b+c, "\n")
         else:
            print(b+d,"\n")

    i += 1
