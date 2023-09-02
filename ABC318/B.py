xy = set()

n = int(input())
for _ in range(n) :
    x1, x2, y1, y2 = map(int, input().split())
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            xy.add((x, y))

print(len(xy))