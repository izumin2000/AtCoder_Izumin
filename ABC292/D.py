from __future__ import print_function

def connected_components(graph):
    seen = set()
    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)

def print_gen(gen):
    print([list(x) for x in gen])

def check_connected(graph):
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(graph.keys())
    for k, v in graph.items():
        for n in v:
            G.add_edge(k, n)
    check = sorted([set(x) for x in nx.connected_components(G)]) == sorted([set(x) for x in connected_components(graph)])
    print(check, "(equal to one derived from networkx)")

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

graph = {}
c = 0
for i in nodes :
    graph[c] = i
    c += 1

# print("graph =", graph)
cc = connected_components(graph)
# print(graph)
cond = True
for g in cc :
    g = list(g)
    cnt = 0
    for node in g :
        cnt += len(graph[node])
    if cnt != len(g) * 2 :
        cond = False

print('Yes' if cond else 'No')