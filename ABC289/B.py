n, m = map(int, input().split())
p = list(map(int, input().split())) + [101]

l = list(range(1, n + 1))
pt = set()
pls = []
for i in range(m) :
    pb, pf = p[i], p[i + 1]
    if (pb + 1) == pf :
        pt.add(pb)
        pt.add(pf)
    else :
        pt.add(pb)
        pls.append(list(pt))
        pt = set()

for pl in pls :
    r = l[min(pl) - 1 : max(pl) + 1][::-1]
    l[min(pl) - 1 : max(pl) + 1] = r
print(*l)