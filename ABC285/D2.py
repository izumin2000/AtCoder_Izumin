n = int(input())    # ノードの数
m = int(input())    # リンクの数

nodes = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(m) :
    s, t = map(int, input().split())    # 各リンクが繋がっているノード
    s -= 1
    t -= 1
    nodes[s].append(t)
    nodes[t].append(s)

def dfs(now, parent=-1):
    visited[now] = True
    for i in nodes[now] :
        # print(now, nodes[now], i, visited)
        if visited[i] :
            if i != parent :
                return True
        else :
            if dfs(i, now) :
                return True
            
    return False

def isCircle() :
    iscircle = False
    while not all(visited) :
        iscircle = dfs(visited.index(False))
        if iscircle :
            break
    return iscircle

print(isCircle())

# 6
# 5
# 1 2
# 2 3
# 4 5
# 5 6
# 4 6

# 5 
# 6
# 1 2
# 1 3
# 2 4
# 3 4
# 3 5
# 4 5