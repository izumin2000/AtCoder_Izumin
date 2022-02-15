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

ans = 0
lst2 = list(range(1, n+1))
for i, j in lst.items() :
    print(i, j)
    if hlist[i - 1] == max(j) :
        ans += 1
        for k in j :
            if k in lst2 :
                lst2.remove(k)
        if i in lst2 :
            lst2.remove(i)
print(lst2)


print(ans+len(lst2))
