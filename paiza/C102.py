dl = ['x'] * 31

n = int(input())
for i in range(n) :
    mi = int(input())
    dl[mi - 1] = 'A'

m = int(input())
for i in range(m) :
    mi = int(input())
    if dl[mi - 1] == 'x' :
        dl[mi - 1] = 'B'
    else :
        dl[mi - 1] += 'B'

b = True
for di in range(31) :
    if dl[di] == "AB" :
        if b :
            dl[di] = 'A'
            b = False
        else :
            dl[di] = 'B'
            b = True

print('\n'.join(dl))