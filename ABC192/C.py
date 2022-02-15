import numpy as np

n, k = map(int, input().split())

def g(l) :
    l = np.sort(l)
    g1 = int("".join(map(str, l.tolist())))
    l = np.sort(l)[::-1]
    g2 = int("".join(map(str, l.tolist())))
    return g2 - g1


for _ in range(k) :
    lst = np.array(list(map(int, list(str(n)))))
    n = g(lst) 

print(n)