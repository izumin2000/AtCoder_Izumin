n = int(input())
l = []
for i in range(n) :
    s, t = map(str, input().split())
    l.append([int(t), s])

l.sort(reverse=True)
print(l[1][1])