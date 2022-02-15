n , m = map(int, input().split())
hlist = list(map(int, input().split()))
lst = {}
for _ in range(m) :
    a , b = map(int, input().split())
    if a in lst.keys() :
        lst[a] += [hlist[b - 1]]
    else :
        lst[a] = [hlist[a - 1], hlist[b - 1]]
    if b in lst.keys() :
        lst[b] += [hlist[a - 1]]
    else :
        lst[b] = [hlist[a - 1], hlist[b - 1]]
lst = sorted(lst)
lack = n - len(lst)
for l in range(lack) :
    lst += (10**5 + l, 10**5 + l)

ans = 0
for k in lst :
    i, j = k
    if hlist[i - 1] == max(j) :
        ans += 1

print(ans)
