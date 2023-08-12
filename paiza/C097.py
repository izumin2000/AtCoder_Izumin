n, x, y  = map(int, input().split())
for i in range(1, n + 1) :
    if not (i % x) :
        if not (i % y) :
            print("AB")
        else :
            print("A")
    else :
        if not (i % y) :
            print("B")
        else :
            print("N")
