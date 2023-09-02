import itertools

n = int(input())
al = list(map(int, input().split()))
bl = [0] * (n + 1)

d = {}
pL = []
ans = 0

for a, i in zip(al, range(n)) :
    if a in d.keys() :
        d[a].append(i)
    else :
        d[a] = [i]

for v in d.values() :
    for i in itertools.combinations(v, 2) :
        pL.append(i)

for a, b in pL :
    ans += (b - a - 1)

for v in d.values() :
    if len(v) >= 3 :
        ans -= sum(range(1, len(v) - 1))

print(ans)