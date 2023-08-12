n = int(input())
al = list(map(int, input().split()))
cl = set([])

for x in range(1, n+1) :
    # print(cl, x, al[x-1])
    if not x in cl :
        cl.add(al[x-1])

nl = set(range(1, n+1)) - cl
nl = sorted(nl)

print(len(nl))
print(*list(nl))