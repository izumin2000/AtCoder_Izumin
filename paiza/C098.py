n = int(input())
l = []
for _ in range(n) :
    l.append(int(input()))

m = int(input())
for _ in range(m) :
    a, b, x = map(int, input().split())
    x = min(l[a - 1], x)
    l[a - 1] = l[a - 1] - x
    l[b - 1] = l[b - 1] + x

print('\n'.join(list(map(str, l))))