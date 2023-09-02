n, d, p = map(int, input().split())
fl = sorted(list(map(int, input().split())), reverse=True)

ans = sum(fl)
ansT = ans
ansL = len(fl)
i = 0
while 1 :
    for _ in range(d) :
        if i >= ansL :
            break
        ansT -= fl[i]
        fl[i] = 0
        i += 1
    ansT += p
    if (ansT <= ans) and (i < ansL) :
        ans = ansT
    else :
        print(min(ans, ansT))
        break