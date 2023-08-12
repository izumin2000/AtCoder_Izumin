r, c = map(int, input().split())

def manhattan(x1, y1, x2, y2) :
    return abs(x1 - x2) + abs(y1 - y2)

l = []
bll = []
h = 0
w = 0
for i in range(r) :
    bl = input()
    bll.append(list(bl))
    for b in bl :
        if b.isdecimal() :
            l.append((w, h, int(b)))
        w += 1
    h += 1
    w = 0

h = 0
w = 0
for bl in bll :
    for b in bl :
        if b.isdecimal() :
            bl[w] = "."
        if b == "#" :
            for i in l :
                xb, yb, d = i
                if manhattan(xb, yb, w, h) <= d :
                    bl[w] = "."
        w += 1
    h += 1
    w = 0

for bl in bll :
    print("".join(bl))