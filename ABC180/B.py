n = int(input())
xl = list(map(int, input().split()))
l = 0
ll = []
for i in xl:
    l += abs(i)
print(l)
l = 0

for i in xl:
    l += i**2
print(l**0.5)

for i in xl:
    ll += [abs(i)]
print(max(ll))