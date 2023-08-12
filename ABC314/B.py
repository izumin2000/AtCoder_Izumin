n = int(input())
all = []
cl = []
for _ in range(n) :
    c = int(input())
    cl.append(c)
    al = list(map(int, input().split()))
    all.append(al)

x = int(input())

d = {}
for i, c, al in zip(list(range(1, n + 1)), cl, all) :
    if x in al :
        d[i] = c

d = [kv for kv in d.items() if kv[1] == min(d.values())]

a = []
for i, _ in d :
    a.append(i)
print(len(a))
print(*a)