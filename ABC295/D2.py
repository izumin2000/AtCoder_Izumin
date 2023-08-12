sl = list(input())
c = 0
for i in range(5*10**5+1) :
    s = sl[::]
    l = list(str(i)*2)
    dl = set()
    dmax = 0
    dmin = 0
    for i in l :
        try :
            j = s.index(i)
        except :
            continue
        else :
            s.pop(j)
            dl.add(s)
            dmax = max(dmax)
        c += 1

print(c)