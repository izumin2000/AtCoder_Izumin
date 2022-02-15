import numpy as np

n = int(input())
la = np.array(list(map(int, input().split())))
lb = np.array(list(map(int, input().split())))
l = np.arange(1001)

for i in range(len(la)) :
    a = la[i]
    b = lb[i]
    il = np.arange(a, b+1)
    l = np.intersect1d(l, il)

print(l.shape[0])

