# cook your dish here

import math
t=int(input())
for i in range(t):
    N,X=map(int,input().split())
    if N==1:
        print(X)
    else:
        print((math.ceil(N/6))*X)