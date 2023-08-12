n = int(input())
al = list(map(int, input().split()))

l = []
for i in range(n-1):
    a, b = al[i], al[i + 1]
    if abs(a - b) == 1 :
        l.append(a)
    else :
        if a < b :
            for j in range(a, b) :
                l.append(j)
        else :
            for j in range(a, b, -1) :
                l.append(j)
l.append(al[-1])
print(*l)