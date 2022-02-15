n, k = map(int, input().split())
c = list(map(int, input().split()))
u = list()

for i in range(n-k+1) :
    u.append(len(set(c[i:i+k])))

print(max(u))