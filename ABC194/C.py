import itertools

n = int(input())
l = list(map(int, input().split()))
x = 0

m = list(itertools.combinations_with_replacement(l, 2))
for j in m :
    y, z = j
    if str(y) == str(z) :
        x += y ** 2 * (n - 1)
    else :
        x -= 2 * y * z

print(x)
