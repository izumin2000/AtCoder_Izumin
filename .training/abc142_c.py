import numpy as np

n = int(input())
n = np.array(np.arange(n))
l = list(map(int, input().split()))

cnt = 1

for i in l :
    n[i-1] = cnt
    cnt += 1

n = np.array(n.tolist(), dtype=int)
print(*n.tolist())


