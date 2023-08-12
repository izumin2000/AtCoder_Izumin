h, w = map(int, input().split())
path = []
bal = [0]
n = 1
for _ in range(h) :
    al = list(map(int, input().split()))
    for j in range(w-1) :
        n += 1
        if al[j] != al[j+1] :
            path.append((n-1, n))
    n -= w
    n += 1
    for j in range(w) :
        n += 1
        if bal[0] :
            if al[j] != bal[j] :
                path.append((n-w, n))
    bal = al

print(path)