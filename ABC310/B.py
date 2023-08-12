n, m = map(int, input().split())
ll = []
for _ in range(n) :
    l = list(map(int, input().split()))
    l[2:] = sorted(l[2:])
    ll.append(l)

ll.sort(reverse=True)
cond = False
for n in range(len(ll) - 1) :
    li, lj = ll[n], ll[n + 1]
    pi, pj = li[0], lj[0]
    fi, fj = set(li[2:]), set(lj[2:])

    # print(f"\033[31m{pi, pj, fi, fj}\033[0m")
    if pi == pj :
        # print(f"\033[31m{1, fi - fj, fj - fi}\033[0m")
        cond = ((len(fi - fj) == 0) and (len(fj - fi) > 0) or ((len(fi - fj) > 0) and (len(fj - fi) == 0)))
    else :
        # print(f"\033[31m{2, fi - fj, fj - fi}\033[0m")
        cond = (fi == fj) or (len(fj - fi) > 0)
    if cond :
        break

print('Yes' if cond else 'No')