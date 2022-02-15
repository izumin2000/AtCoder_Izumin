#import numpy as np

a, b, c = map(int, input().split())
cnt = 0

if a == b == c and a%2 == 0:
    print(-1)
else :
    while a%2 == 0 and b%2 == 0 and c%2 == 0 :
        A = b/2 + c/2
        B = a/2 + c/2
        C = a/2 + b/2
        a = A
        b = B
        c = C
        cnt += 1
    print(cnt)