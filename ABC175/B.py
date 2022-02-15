import itertools

n = int(input())
l = list(map(int, input().split()))
cnt = 0
for a, b, c in itertools.combinations(l, 3) :
    if max([a, b, c]) < (sum([a, b, c]) - max([a, b, c])) :
        if len([a, b, c]) == len(set([a, b, c])) :
            cnt += 1
print(cnt)