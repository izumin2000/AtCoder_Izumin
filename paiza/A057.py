def chain(l) :
    r = 1
    n = 1
    j = l[0]
    for i in l[1:] :
        if i == j + 1 :
            n += 1
            r = max(r, n)
        else :
            n = 1
        j = i
    
    n = 1
    j = l[-1]
    for i in l[-2::-1] :
        if i == j + 1 :
            n += 1
            r = max(r, n)
        else :
            n = 1
        j = i

    return r

def tate(l) :
    n = len(l)
    r = []
    for i in range(n) :
        rr = []
        for j in range(n) :
            rr.append(l[n - j - 1][i])
        r.append(rr)
    return r

def naname(l) :
    n = len(l)
    r = []
    for i in range(n) :
        rr1 = []
        rr2 = []
        for j in range(n - i) :
            rr1.append(l[i + j][j])
            rr2.append(l[j][i + j])
        r.append(rr1)
        r.append(rr2)
    return r


n = int(input())
r = 0
sl = []
for _ in range(n) :
    l = list(map(int, input()))
    r = max(r, chain(l))
    sl.append(l)
ll = tate(sl)
for l in ll :
    r = max(r, chain(l))

ll = naname(sl)
for l in ll :
    r = max(r, chain(l))

ll = naname(tate(sl))
for l in ll :
    r = max(r, chain(l))

print(r)