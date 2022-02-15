import math

n = int(input())
l = list(map(int, input().split()))

mx = max(l) + 1
cnt = [0] * mx

for c in l:
    i = 1
    while i * i <= c:
        if c % i == 0:
            cnt[i] += 1
            if i * i != c:
                cnt[c // i] += 1
        i += 1

for i in range(mx - 1, 0, -1):
    if cnt[i] > 1:
        print(i)
        break