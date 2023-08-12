def pi(s) :
    s = str(s)
    n = 1
    for t in s :
        n *= int(t)
    return n

l = 0
for i in range(1000000) :
    j = 0
    while 1 :
        p = pi(i)
        j += 1
        if p > 9 :
            i = p
        else :
            if j == 5 :
                l += 1
            break
print(l)