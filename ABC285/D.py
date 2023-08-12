import networkx as nx

n = int(input())
Graph = nx.DiGraph()

for i in range(n) :
    s, t = map(str, input().split())
    Graph.add_node(s)
    Graph.add_node(t)
    Graph.add_edge(s, t)

try :
    cond = nx.eulerian_circuit(Graph)
except :
    print("Yes")
else :
    print("No")