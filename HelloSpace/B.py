n, d, h = map(int, input().split())
l = []

for i in range(n) :
    wd, wh = map(int, input().split())
    l += [(wh - h) / (wd - d)]

a = min(l)
#print(l)
r = h - a * d
#print(h, a, d)
if r <= 0 :
    print(0)
else :
    print(r)