h, w, k = map(int, input().split())
res = 0
yoko = [0]
tate = [0]*(w+1)
for _ in range(h) :
    s = input()
    yoko.append(s.count("#"))
    for i in range(len(s)) :
        if s[i] == "#" :
            tate[i+1] += 1

print(yoko, tate)
for y in yoko :
    for t in tate :
        if (sum(yoko) - y - t) == k :
            print(y, t)
            res += 1
print(res)