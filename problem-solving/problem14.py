n = int(input())

i = 0
while (i < n):
    a, b, c, d = map(int, input().split())
    s1 = a-c
    s2 = b-d
    if (s1 < s2):
        print("First\n")
    elif (s2 < s1):
        print("Second\n")
    elif(s1==s2):
        print("Any\n")

    i += 1
