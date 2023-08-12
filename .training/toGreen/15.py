n, w = map(int, input().split())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

l.sort(reverse=True)
c = 0
ans = 0
last = (0, _)
for i in l :
    a, b = i
    c += b
    ans += a * b
    if c > w :
        last = i
        break

a, b = last
snip = a * (w - c)
print(ans + snip)