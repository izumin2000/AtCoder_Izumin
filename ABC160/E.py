x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

pq = sorted(p + q, reverse=True)
pr = sorted(p + r, reverse=True)
qr = sorted(q + r, reverse=True)
pqr = sorted(p + q + r, reverse=True)





