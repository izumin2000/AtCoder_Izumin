n, m = map(int, input().split())

sl = []
for i in range(n) :
    sl.append(input())

tl = []
for j in range(m) :
    tl.append(input())

a = 0
tl = list(set(tl))
for i in sl :
    for j in tl :
        if i[3:] == j :
            a += 1

print(a)