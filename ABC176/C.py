n = int(input())
al = list(map(int, input().split()))
max = 0
r = 0
for x in al :
    if max < x :
        max = x
    else :
        r += max - x
print(r)

