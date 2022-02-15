#J - リストにいるEnryoさん

"""
動的計画法で調べてみよう！
"""
n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
 
dp = [-1000000000] * (n + 1)
dp[0] = 0
 
for i in range(n):
    dp[i + 1] = max(dp[i + 1], dp[i] - x + a[i + 1])
 
    if i + 2 <= n:
        dp[i + 2] = max(dp[i + 2], dp[i] - y + a[i + 2])
 
    if i == 0:
        continue
    d = 2
 
    while i * d <= n:
        dp[d * i] = max(dp[d * i], dp[i] - z + a[d * i])
        d += 1
 
print(dp[n])