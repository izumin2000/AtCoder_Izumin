a,b,c,d = map(int, input().split())
w = a
r = 0
l = 0

if b > c :
    print(-1)

if d == 1 :
    print(-1)

else :
    while True :
        w += b
        r += c
        l += 1
        #print(w, r)
        mul = w / r 
        if mul < d :
            break

    print(l)
