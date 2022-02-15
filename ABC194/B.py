n = int(input())
al = []
bl = []
for i in range(n) :
    a, b = map(int, input().split())
    al += [a]
    bl += [b]
    
pa = al.index(min(al))
pb = bl.index(min(bl))
r1 = 20001
r2 = 20001
r3 = 20001
r4 = 20001
if pa != pb :
    r1 = max([min(al), min(bl)])
else :
    dal = al[:]
    dbl = bl[:]
    dal.remove(min(al))
    dbl.remove(min(bl))
    r2 = min(al)+min(bl)
    r3 = max([min(dal), min(bl)])
    r4 = max([min(al), min(dbl)])

print(min([r1, r2, r3, r4]))


    

