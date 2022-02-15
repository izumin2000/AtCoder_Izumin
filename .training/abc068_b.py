import numpy as np

n = int(input())
if n%2 == 0:
    nl = [True, False]*int(n/2)
else :
    nl = [True, False]*int(n/2)+[True]

al = np.sort(np.array(list(map(int, input().split()))))[::-1]

Alice = np.where(nl, al, 0)
Bob = np.where(nl, 0, al)

print(np.sum(Alice) - np.sum(Bob))