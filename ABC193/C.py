import numpy as np

n = int(input())
nl = np.array(list(range(1, n+1)))
l = np.array([])
rng = range(2, int(n ** 0.5) + 1)
#y = 2
for i in rng :
    print((i ** np.array(rng)))
    l = np.append((i ** np.array(rng)), l)
    #nl = nl[~(nl == i ** np.array(rng))]
    #print(nl)
    #while i ** y <= n :
        #y += 1
    #y = 2

l = np.unique(l)
print(n - l.size)
