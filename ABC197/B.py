h, w, x, y = map(int, input().split())
r = 0
n = 0
xl = []
yl = []
for _ in range(h) :
    s = list(input())
    yl += [s[y-1]]
    if n == (x-1) :
        xl = s
    n += 1

print(xl, yl)
for px in range(x-1, w) :
    if xl[px] == "." :
        r += 1
    else :
        break

for mx in list(range(0, x-1))[::-1] :
    if xl[mx] == "." :
        r += 1
    else :
        break

for py in range(y, h) :
    if yl[py] == "." :
        r += 1
    else :
        break

for my in list(range(0, y))[::-1]  :
    if yl[my] == "." :
        r += 1
    else :
        break

if h == 1 :
    r += 1
if w == 1 :
    r += 1

print(r-3)