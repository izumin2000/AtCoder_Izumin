n, k = map(int, input().split())

c = 0
l = []
for i in range(n) :
    s = input()
    if c < k :
        l.append(s)
    c += 1

ll = sorted(l)
for i in ll :
    print(i)