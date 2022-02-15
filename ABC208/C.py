import numpy as np

n, k = map(int, input().split())
l = np.array(list(map(int, input().split())))

r = np.array([k//n]*n)

a = k%n
if a :
    sl = np.sort(l)

    give = sl[:a]
    r[np.isin(l, give)] = r[np.isin(l, give)] + 1

    #print(a, sl, give, ll)

for i in r.tolist() :
    print(i)
