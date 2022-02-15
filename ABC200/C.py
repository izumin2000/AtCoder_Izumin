import itertools
import numpy as np
import math

n = int(input())
l = np.array(list(map(int, input().split())))
mod = l % 100
#print(mod)
u, counts = np.unique(mod, return_counts=True)
#print(u, counts)

cnt = 0
for d in u :
    #print(d)
    div = l[(l % 100) == d]
    odd = div[((div // 100) % 2) == 0].shape[0]
    even = div[((div // 100) % 2) == 1].shape[0]
    #print(div[((div // 100) % 2) == 0])
    #print(div[((div // 100) % 2) == 1])
    if odd > 1 :
        cnt += math.factorial(odd) // (math.factorial(odd - 2) * math.factorial(2))
    if even > 1 :
        cnt += math.factorial(even) // (math.factorial(even - 2) * math.factorial(2))
        
"""
mod = mod.tolist()
for x in u :
    #print(x)
    mod.remove(x)
#print(mod)

mod = np.array(mod)
div = np.unique(mod)
#print(div)

edit = np.array([])
for d in div :
    new = l[(l % 100) == d]
    edit = np.append(edit, new)
#print(edit)

cnt = 0

for (i, j) in itertools.combinations(l, 2):
    #print(i, j)
    if ((i - j)%200) == 0 :
        cnt += 1
"""
print(cnt)