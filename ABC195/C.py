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
    xl = np.array([n+1])
    for i in range(c-1) :
        xl = np.append(xl, (1000**(c-i-1)) - (1000**(c-i-2)))
    r = np.sum(l * xl)
    print(l, xl)
    print(r)