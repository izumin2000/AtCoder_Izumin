import numpy as np
l = []
n = int(input())
for i in range(n) :
    l += [list(map(int, input().split()))]

l = np.array(l)
r = l.max(axis = 0)
#print(r)
print(r.min())