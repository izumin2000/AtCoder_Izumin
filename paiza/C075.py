n, m = map(int, input().split())
p = 0
for _ in range(m) :
    t = int(input())
    if p >= t :
        p -= t
    else :
        p += int(t / 10)
        n -= t
    print(f"{n} {p}")