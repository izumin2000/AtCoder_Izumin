n, a, b = map(int, input().split())
amari = n % (a+b)
if amari > a :
    amari = a
print((n // (a+b)) * a + amari )