n, q = map(int, input().split())

l = [0] * n
for i in range(q) :
    e, p = map(int, input().split())
    if e == 1 :
        l[p - 1] += 1
    elif e == 2 :
        l[p - 1] += 2
    else :
        cond = l[p - 1] >= 2
        print('Yes' if cond else 'No')
