n, a, b = map(int, input().split())

deff = b - a
distBN = n - b

def half(A, B) :
    return int((B - A)/2)

def Bool(A, B) :
    return (B - A)%2 == 0

if Bool(a, b) :
    print(half(a, b))
else :
    resultA = n - b + 1 + half(n + a - b + 1, n)
    resultB = a + half(1, b - a)
    if resultA > resultB :
        print(resultB)
    else :
        print(resultA)
