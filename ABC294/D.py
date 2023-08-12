n, q = map(int, input().split())
c = set()
u = set()
i = 1
for i in range(q) :
    s = input()
    if s[0] == "1" :
        p = u.pop(i)
        c.add(p)
    if s[0] == "2" :
        x = s[2]

    if s[0] == "3" :