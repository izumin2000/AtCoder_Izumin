n = int(input())
l = set()
for _ in range(n) :
    (a, b) = input().split()
    l.add((a, b))
if len(l) == n :
    print("No")
else :
    print("Yes")