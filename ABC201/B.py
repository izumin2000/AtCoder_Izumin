import numpy as np
sl = np.array([])
tl = np.array([])
n = int(input())

for i in range(n) :
    s, t = input().split()
    sl = np.append(sl, s)
    tl = np.append(tl, int(t))

stl = np.sort(tl)[::-1]
#print(stl)
sec = stl[1]
#print(sec)
ll = np.arange(len(tl))[tl == sec]
#print(ll)
print(*sl[ll].tolist())