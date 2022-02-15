n = int(input())
l = list(map(int, input().split()))
ll = sorted(l)
if list(range(1, n+1)) == ll :
    print("Yes")
else :
    print("No")