a, x, m = map(int, input().split())
loop = []
b = a%m
c = b - m
print(a, b, c)
for i in range(m-1) :
    n = (b**i)%m
    loop.append(n)

n = (sum(loop)%m) * (x//len(loop))
n += sum(loop[:(x%len(loop))])
print(n%m)