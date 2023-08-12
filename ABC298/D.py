n = int(input())

ql = []
for _ in range(n) :
    ql.append(input())

n = m = 0
nn = ""
for q in ql :
    if q[0] == "1" :
        n += 1
        