n , x = map(int, input().split())
al = 0.0
r = 0
b = True
for i in range(n) :
    v, p = map(int, input().split())
    al += 0.01 * v * p
    if (al > x) and b:
        r = 1 + i
        b = False
if b:
    print(-1)
else :
    print(r)