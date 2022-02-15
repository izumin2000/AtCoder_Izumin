import numpy as np

n = int(input())

u = np.array([])
b = np.array([])

for _ in range(n) :
    t, l, r = map(int, input().split())
    u = np.append(u, l)
    b = np.append(b, r)

for i in range(n) :
    mi = u[i]
    
