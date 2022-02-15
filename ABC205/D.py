import sys

n, q = map(int, input().split())
al = list(map(int, input().split()))
tmp = 0
r = []

for i in al :
    if (i - tmp) != 1 :
        r.append(i - tmp - 1)
    tmp = i

r.append(10**18 - al[-1])
print(r)
sys.exit()

kl = []
for _ in range(q) :
    kl.append(int(input()))

for j in r :
    k = int(input())
    ts = len(al[al <= k])
    r.append(ts + k)

print(r)