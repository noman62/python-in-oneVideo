n = int(input())

i = 0
while (i < n):
    a, b= map(int, input().split())
    if (a >= b):
        print("Yes\n")
    else:
        print("No\n")
    i += 1
