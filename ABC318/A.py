n, m, p = map(int, input().split())
c = 0


for i in range(1, n + 1) :
    if (i >= m) and (((i - m) % p) == 0) :
        c += 1

print(c)