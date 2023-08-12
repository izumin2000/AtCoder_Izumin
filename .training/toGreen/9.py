x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if (x2 != x3) and (y2 != y3) :
    if x1 == x2 :
        print(x3, y2)
    else :
        print(x2, y3)
if (x3 != x1) and (y3 != y1) :
    if x2 == x3 :
        print(x1, y3)
    else :
        print(x3, y1)
if (x1 != x2) and (y1 != y2) :
    if x3 == x1 :
        print(x2, y1)
    else :
        print(x1, y2)
