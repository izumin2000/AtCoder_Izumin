def to10(x, k) :
    d = len(x) - 1
    r = 0
    for i in x :
        r += int(i) * (k ** d)
        d -= 1
    return r

k = int(input())
a, b = input().split()

print(to10(a, k) * to10(b, k))