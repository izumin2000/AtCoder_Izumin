n = int(input())

rlist = []
blist = []

for _ in range(0, n) :
    xc = list(input().split())
    if xc[1] == "R" :
        rlist += [int(xc[0])]
    else :
        blist += [int(xc[0])]

result = sorted(rlist) + sorted(blist)
for i in result :
    print(i)

