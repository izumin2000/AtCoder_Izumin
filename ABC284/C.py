n, m = map(int, input().split())

gs = []
s = set()
for i in range(m) :
    v, w = map(int, input().split())
    if (v in s) or (w in s) :
        i = 0
        for g in gs :
            if (v in g) or (w in g) :
                gs[i].add(v)
                gs[i].add(w)
            i += 1
    else :
        gs.append(set([v, w]))

    s.add(v)
    s.add(w)

a = 0
for i in gs :
    a += 1

print(a + n - len(s))
print(gs, s)