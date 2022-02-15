n  = int(input())
#l = []
pl = []
for _ in range(n) :
    a, p, x = map(int, input().split())
    if x-a > 0 :
        #l += [x-a]
        pl += [p]

if len(pl) == 0 :
    print(-1)
else :
    #r = pl.index(min(pl))
    print(min(pl))
