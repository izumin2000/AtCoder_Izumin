from collections import deque

n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = al + bl
cl.sort()
ad = deque(al)
bd = deque(bl)

cond = True

ansA = []
ansB = []
i = 1
for c in cl :
    if len(ad) :
        if c == ad[0] :
            ansA.append(i)
            ad.popleft()
    if len(bd) :
        if c == bd[0] :
            ansB.append(i)
            bd.popleft()
    i += 1

print(*list(ansA))
print(*list(ansB))