# 3
# 7 5 12
# 10 6 20
# 12 3 8

n = int(input())
maxt = 0
mint = 48
for _ in range(n) :
    s, f, t = map(int, input().split())
    t = s + f + 24 - t
    maxt = max(maxt, t)
    mint = min(mint, t)

print(mint)
print(maxt)