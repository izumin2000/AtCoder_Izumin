n , x = map(int, input().split())
al = 0.0
b = True
for i in range(n) :
    v, p = map(int, input().split())
    al += 0.01 * v * p
    if al > x and b:
        print(n + 1)
if not b:
    print(-1)
