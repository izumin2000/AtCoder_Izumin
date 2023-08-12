def f(s, x, c) :
    x = int(x)
    return s[:x] + c + s[x:]

_ = int(input())
s = input()
n = int(input())
upper = 0
p = 0
l = []
for i in range(n) :
    t, x, c = map(str, input().split())
    if t in "23" :
        upper = t
        p = i
    else :
        l.append((i, int(x) - 1, c))

print(f"\033[31m{p, upper, l}\033[0m")
b = True
for i, x, c in l :
    s = f(s, x, c)
    if p > i :
        if b :
            if upper == "2" :
                s = s.lower()
            if upper == "3" :
                s = s.upper()
            b = False
print("".join(s))