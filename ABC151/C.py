ac = 0
wa = 0
check = []

n, m = map(int, input().split())
for _ in range(m) :
    p, s = map(str, input().split())
    if not int(p) in check :
        if s == "WA" :
            wa += 1
        else :
            ac += 1
            check += [int(p)]

print(ac, wa)
