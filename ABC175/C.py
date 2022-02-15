x, k, d = map(int, input().split())    
if x > 0 :
    if x - k * d > 0 :
        print(x - k * d)
    else :
        a = x%d
        b = abs(a - d)
        if (x%d == 0) & (k - (x//d))%2 == 1 :
            print(d)
        elif a <= b :
            print(a)
        else :
            print(b)
else :
    if x - k * d < 0 :
        print(k * d - x)
    else :
        a = x%d
        b = abs(a - d)
        if (x%d == 0) & (k + (x//d))%2 == 1 :
            print(d)
        elif a <= b :
            print(a)
        else :
            print(b)