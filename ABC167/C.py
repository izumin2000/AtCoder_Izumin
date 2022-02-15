import itertools
n, m, x = map(int, input().split())

dict = {}
for i in range(n) :
    ca = list(map(int, input().split()))
    dict[ca[0]] = ca[1:]
print(dict)
for j in range(n) :
    for k in list(itertools.combinations(dict.values(), j+1)) :
        k
