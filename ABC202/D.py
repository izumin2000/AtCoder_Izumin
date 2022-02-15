n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

bic = [b[ci - 1] for ci in c] 

la = [0] * n
lb = [0] * n
cnt = 0

for ai in a :
    la[ai-1] += 1

for bi in bic :
    lb[bi-1] += 1

for i in range(n) :
    cnt += (la[i] * lb[i])

print(cnt)