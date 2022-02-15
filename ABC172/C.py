n, m, k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
sb = []

rl = []

for i in range(n+1) :
    As = sum(al[:i+1])
    if As >= k :
        break
for j in range(m+1) :
    Bs = sum(bl[:j+1])
    if As + Bs < k :
        rl += [i+j]
    else :
        break

if rl == [] :
    print(0)
else :
    print(max(rl) + 2)
