import itertools
n = input()
result = 0
for a, b in itertools.combinations(range(len(n)+1), 2) :
    if b - a > 3 :
        if int(n[a:b])%2019 == 0 :
            result += 1

print(result)