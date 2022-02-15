import numpy as np

n = int(input())
al = np.array(list(map(int, input().split())))
bl = np.array(list(map(int, input().split())))
cl = np.array(list(map(int, input().split())))
bi = np.array([])
cnt = 0

for x in cl :
    bi = np.append(bi, bl[x-1])
#print(bi)

dup = np.intersect1d(al, bi)
ak = np.in1d(al, dup)
bk = np.in1d(bi, dup)
#print(dup, ak, bk)

a = al[ak]
b = bi[bk]
#print(a, b)

au, acounts = np.unique(a, return_counts=True)
bu, bcounts = np.unique(b, return_counts=True)

au = np.array(au)
bu = np.array(bu)
acounts = np.array(acounts)
bcounts = np.array(bcounts)

for aui in range(au.shape[0]) :
    cnt += (acounts[aui] * bcounts[aui])

print(cnt)