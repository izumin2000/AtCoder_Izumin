import numpy as np

l = np.array(list(input()))

os = np.arange(10)[l == 'o']
qs = np.arange(10)[l == 'q']
xs = np.arange(10)[l == 'x']
cnt = 0

for i in range(10000) :
    if i < 10 :
        c = np.array([0,0,0,i])
    elif i < 100 :
        s = str(i)
        c = np.array([0,0,int(s[1]),int(s[0])])
    elif i < 1000 :
        s = str(i)
        c = np.array([0,int(s[2]),int(s[1]),int(s[0])])
    else :
        s = str(i)
        c = np.array([int(s[3]),int(s[2]),int(s[1]),int(s[0])])
    
    #x check
    x = np.intersect1d(c, xs)
    if x.shape[0] > 0 :
        continue

    #o check
    o = np.intersect1d(c, os)
    if o.shape[0] != os.shape[0] :
        continue

    #q check 
    for q in qs :
        #print(q)
        if not(q in c) :
            continue
    
    cnt += 1

print(cnt)