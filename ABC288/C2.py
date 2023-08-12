n, m = map(int, input().split())
nodes = [[] for _ in range(n)]
visited = [False for _ in range(n)]
newvisit = set()

for i in range(m) :
    s, t = map(int, input().split())    # 各リンクが繋がっているノード
    s -= 1
    t -= 1
    nodes[s].append(t)
    nodes[t].append(s)

def glaph(nodes) :
    c = 0
    for i in nodes:
        if len(i) :
            c += 1
    return c

def links(nodes) :
    c = 0
    for i in nodes :
        c += len(i)
    return c

n = int((links(nodes) - (glaph(nodes) - 1) * 2) / 2)
if n > 0 :
    print(n)
else :
    print(0)
