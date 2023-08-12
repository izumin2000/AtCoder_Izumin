from collections import Counter

n, m = map(int, input().split())

cond = True

s = ""
for _ in range(m) :
    u, v = map(int, input().split())
    s += str(u) + str(v)

if (n - m) != 1 :
    cond = False

st = 0
for i in Counter(s).values() :
    if i > 2 :
        cond = False
    if i == 1 :
        st = i

# length, _ = nx.single_source_dijkstra(Graph, sg[0])
# if len(length) != n :
#     cond = False
# length, _ = nx.single_source_dijkstra(Graph, sg[1])
# if len(length) != n :
#     cond = False


print('Yes' if cond else 'No')