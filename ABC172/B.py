s = input()
t = input()
n = len(s)
for i in list(range(n)) :
    if s[i] == t[i] :
        n -= 1

print(n)