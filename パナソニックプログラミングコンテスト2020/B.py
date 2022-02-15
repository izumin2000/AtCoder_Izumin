h, w = map(int, input().split())
if h%2 == 0 :
    print(int(h*w/2))
else :
    if w%2 == 1 :
        print(int(h*w/2) + 1)
    else :
        print(int(h*w/2))