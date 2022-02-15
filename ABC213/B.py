n = int(input())
a = list(map(int, input().split()))

x = sorted(a)[::-1][1]
print(a.index(x)+1)
