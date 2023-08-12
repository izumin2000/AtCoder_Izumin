n, p, q = map(int, input().split())
dl = list(map(int, input().split()))

d = min(dl)
print(min(p, q + d))