n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = []
for a in al :
    cl.append((a, 'A'))
for b in bl :
    cl.append((b, 'B'))

cl.sort()

ansA = []
ansB = []
i = 1
for c in cl :
    _, ab = c
    if ab == "A" :
        ansA.append(i)
    else :
        ansB.append(i)
    i += 1

print(*ansA)
print(*ansB)