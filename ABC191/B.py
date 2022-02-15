import numpy as np

n, x = map(int, input().split())
l = np.array(list(map(int, input().split())))
r = l[l != x]

print(*r.tolist())