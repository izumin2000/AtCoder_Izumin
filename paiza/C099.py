n, d = map(int, input().split())
l = d
for _ in range(n - 1) :
    dn = int(input())
    l += d - dn
print(l * d)
