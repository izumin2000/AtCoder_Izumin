from collections import defaultdict

n = int(input())
q = int(input())
ns = [[] for _ in range(n+1)]
ss = defaultdict(set)
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1 :
        n = s[1]
        box = s[2]
        ns[box].append(n)
        ss[n].add(box)
    if s[0] == 2 :
        n = s[1]
        print(*list(sorted(ns[n])))
    if s[0] == 3 :
        n = s[1]
        print(*list(sorted(ss[n])))