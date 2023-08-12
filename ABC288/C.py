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

def dfs(now):
    visited[now] = True
    newvisit.add(now)
    for i in nodes[now]:
        if not visited[i]:
            dfs(i)

def links(nodes) :
    c = 0
    for i in nodes :
        c += len(i)
    return c

ans = 0
dfs(0)
while 1 :
    l = []
    for edge in newvisit :
        l.append(nodes[edge])
        
    n = int((links(l) - (len(newvisit) - 1) * 2) / 2)
    if n > 0 :
        ans += n
    if all(visited) :
        break
    else :
        newvisit = set()
        dfs(visited.index(False))

print(ans)