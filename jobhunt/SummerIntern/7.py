import string

n = 48
l = [[''] * n] * n
a = list(string.ascii_uppercase)
al = len(a)
s = a * (int((n * n) / al) + 1)
s = s[:(n * n)]

ans = "A"
i = 2 * n - 3
j = 0
while i:
    ans += s[i] + s[i * 2]
    i -= 2
    J = i

print(s)