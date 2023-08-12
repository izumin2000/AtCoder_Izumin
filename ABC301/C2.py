sl = list(input())
tl = list(input())
atcoder = list("atcoder")

for s in sl[::] :
    if (s in tl) and (s != "@") :
        sl.remove(s)
        tl.remove(s)

print(f"\033[31m{sl, tl}\033[0m")
atmarks = sl.count("@") + tl.count("@")
atcoders = 0
cond = True
for i in range(len(sl)):
    si, ti = sl[i], tl[i]
    if si in atcoder :
        atcoders += 1
    elif (si != "@") :
        cond = False
    if ti in atcoder :
        atcoders += 1
    elif (ti != "@") :
        cond = False

if atcoders > atmarks :
    cond = False

print('Yes' if cond else 'No')