n, m = map(int, input().split())
a = sum(list(map(int, input().split())))

if a > n:
    print(-1)
else :
    print(n - a)