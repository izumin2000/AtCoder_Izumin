import itertools
n = int(input())
l = []
for _ in range(n) :
    x, y = map(int, input().split())
    l.append((x, y))

m = 0
for pair in itertools.combinations(l, 2) :
    (x1, y1), (x2, y2) = pair[0], pair[1]
    m = max(m, ((x1 - x2)**2 + (y1 - y2)**2)**0.5)
print(m)