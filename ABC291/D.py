n = int(input())
bi, bj = map(int, input().split())
left, right = 1, 1
for _ in range(n-1) :
    i, j = map(int, input().split())
    leftt, rightt = 0, 0
    if bi != i :
        leftt += left
    if bj != i :
        leftt += right
    if bi != j :
        rightt += left
    if bj != j :
        rightt += right

    left, right = leftt, rightt
    bi, bj = i, j

print((left+right)%998244353)