visited = [False] * 6
nodes = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]]

def dfs(now):
    visited[now] = True
    for i in nodes[now]:
        if not visited[i]:
            dfs(i)

print(visited)