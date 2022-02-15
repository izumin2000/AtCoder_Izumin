import collections

n = int(input())
result = []
for _ in range(n) :
    thing = input()
    result += [thing]
print(len(collections.Counter(result)))