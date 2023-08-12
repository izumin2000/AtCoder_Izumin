m, p, q = map(int, input().split())
x = m * p / 100
y = (m - x) * q / 100
print(m - x - y)