n = int(input())
l = list(map(int, input().split()))
x = int(input())

ans = (x//sum(l)) * n
total = (x//sum(l)) * sum(l)

i = 0
if x%sum(l) :
    while total <= x :
        total += l[i]
        i += 1
    print(ans + i)

else :
    print(ans + 1)