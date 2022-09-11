n = int(input())

i = 0
while (i < n):
    a, b = map(int, input().split())
    if (a == b):
        print("Yes\n")
    elif (a < b):
        s1 = a
        while True:
            s1 = s1*2
            if (s1 == b):
                print("Yes\n")
                break
            elif (s1 > b):
                print("No\n")
                break
    elif (a > b):
        s2 = b
        while True:
            s2 = s2*2
            if (s2 == a):
                print("Yes\n")
                break
            elif (s2 > a):
                print("No\n")
                break
    i += 1
