f = True
n, s, d = map(int, input().split())
for i in range(n) :
    x, y = map(int, input().split())
    if (x < s) and (y > d) and f:
        print("Yes")
        f = False
if f :
    print("No")