import numpy as np

to = input()
n = int(to)
d = len(to)

ln = len(str(n))
c = int((ln-1)//3)

if c == 0 :
    print(0)
else :
    l = np.array(np.arange(1, c+1))[::-1]
    dd = d%3
    if dd == 0 :
        dd = 3
    xl = np.array([int(to[:dd])])
    for i in range(c-1) :
        #print((c-i)*-3, -3*(c-i-1))
        apnd = int(to[-3*(c-i) : -3*(c-i-1)])
        if apnd == 0 :
            apnd = 1000
        xl = np.append(xl, [])
    print(xl)
"""
    r = np.sum(l * xl)
    print(r)"""