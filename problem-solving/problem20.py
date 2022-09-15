n = int(input())

i = 0
while (i < n):
    a, b = map(int, input().split())
    if (a >= b):
        print(b,"\n")
    else:
        print(a,"\n")

    i += 1
