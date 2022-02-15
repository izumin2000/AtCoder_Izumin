a, b, n = map(int, input().split())

x = 0
step = int(b/a)
if step == 0 :
    step = 1
while x <= n:
    ans1 = int(a*x/b) - a * int(x/b)
    x += step
    ans2 = int(a*x/b) - a * int(x/b)
    if ans1 > ans2:
        break
print(ans1)
