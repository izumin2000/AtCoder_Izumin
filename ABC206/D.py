import numpy as np

n = int(input())
l = list(map(int, input().split()))
wa = []

n = int(n/2)
for i in range(n) :
    hd = l[i]
    tl = l[-1 * i - 1]
    if hd != tl :
        wa.append(hd)
        wa.append(tl)

wal = int(len(wa) / 2)
u = np.unique(wa)
if n == 0 :
    print(0)
elif len(u) == wal:
    print(wal-1)
else :
    print(wal)