import numpy as np

s = np.array(list(input()))
la = np.arange(len(s))[s == "A"]
lt = np.arange(len(s))[s == "T"]
lg = np.arange(len(s))[s == "G"]
lc = np.arange(len(s))[s == "C"]

la = np.append(la, lt)
la = np.append(la, lg)
la = np.append(la, lc)

if np.shape(la)[0] == 0 :
    print(0)
else :
    la = np.sort(la)
    tmp = la[0]
    cnt = 0
    r = []

    la = np.append(la, 11)

    for i in la.tolist()[1:] :
        if tmp == i-1 :
            cnt += 1        
        else :
            r.append(cnt+1)
            cnt = 0

        tmp = i

    if len(r) == 0 :
        print(0)
    else  :
        print(max(r))
