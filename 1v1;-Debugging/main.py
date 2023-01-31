t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = (a * b) - (a + b)
    for j in range(c):
        if j == c:
            print(a)
        else:
            break
    else:
        print(c)