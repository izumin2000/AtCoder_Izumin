import sys

a, b, c, k = map(int, input().split())
ans = 0
if k <= a :
    print(k)
    sys.exit()
else :
    ans += a
    k -= a

if k <= b :
    print(ans)
    sys.exit()
else :
    k -= b
    ans -= k

print(ans)