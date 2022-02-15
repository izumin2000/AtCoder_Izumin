a, b, n = map(int, input().split())

x = 0
step = int(b/a)
if step == 0 :
    step = 1
while x <= n:
    ans1 = int(a*x/b) + a*int(x/b)
    ans2 = int(a*(a+1)/b) + a*int((x+1/b))
    if ans2 - ans1 >= 0 :
        x += step
    else:
        break
if  n == (x-1) :
    x -= 1
print(int(a*x/b) - a*int(x/b))