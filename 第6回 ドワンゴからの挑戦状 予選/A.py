n = int(input())
sList = []
tLsit = []
result = 0
count = 0
Bool = False
for _ in range(n) :
    s, t = map(str, input().split())
    sList += [s]
    tLsit += [int(t)]
x = input()

for S in sList :
    if Bool :
        result += tLsit[count]
    if S == x :
        Bool = True
    count += 1

print(result)



