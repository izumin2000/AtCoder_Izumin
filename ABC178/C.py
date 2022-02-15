import math
n = int(input())
if n > 2 :
    a = (math.factorial(n) // math.factorial(n-2)) * int(10 ** (n - 3) * 81)
    print(a%(10**9+7))
elif n == 2:
    print(2)
else :
    print(0)