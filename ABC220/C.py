n = int(input())
il = list(map(int, input().split()))
x = int(input())
sm = sum(il)

d = int(x / sm)
result = d * n
al = sm * d
i = 0
while (al <= x) :
    result += 1
    al += il[i%n]
    i += 1

print(result)