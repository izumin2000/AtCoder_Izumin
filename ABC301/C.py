s = input()
t = input()

atcoder = list("atcoder")
cond = True
for i in range(len(s)):
    a, b = s[i], t[i]
    if (a == "@") and (b != "@") :
        if not b in atcoder :
            cond = False
    if (a != "@") and (b == "@") :
        if not a in atcoder :
            cond = False

if not(s.count("@")) and not(t.count("@")) :
    if s != t :
        cond = False

print('Yes' if cond else 'No')