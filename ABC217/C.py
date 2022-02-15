import bisect

n = int(input())
l = list(map(int, input().split()))

r = [0] * n
n = 1
for i in l:
    r[i - 1] = n
    n += 1

print(*r)