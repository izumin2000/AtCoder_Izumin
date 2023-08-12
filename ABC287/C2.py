import networkx as nx

n, m = map(int, input().split())
Graph = nx.Graph()

if (n - m) != 1 :
    cond = False

for _ in range(m) :
    s, t = map(int, input().split())
    Graph.add_node(s)
    Graph.add_node(t)
    Graph.add_edge(s, t)

try :
    nx.find_cycle(Graph)
except :
    cond = True and cond
else :
    cond = False

print('Yes' if cond else 'No')