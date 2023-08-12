import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
nodes = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].append(v)
    nodes[v].append(u)


visited = [False for _ in range(n)]
def dfs(now):
    visited[now] = True
    for i in nodes[now]:
        if not visited[i]:
            dfs(i)

dfs(0)
    
cond = all(visited)
ones = 0
twos = 0
for j in [len(i) for i in nodes] :
    if j == 1 :
        ones += 1
    elif j == 2 :
        twos += 1
    else :
        cond = False

if ones != 2 :
    cond = False
if twos != (n - 2) :
    cond = False
    
print('Yes' if cond else 'No')