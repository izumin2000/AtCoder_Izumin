def abc(s) :
    return ord(s) - ord("a")

sl, tl = list(input()), list(input())
sabc, tabc = [0] * (abc("z") + 1), [0] * (abc("z") + 1)
atcoder = list("atcoder")
atcoderi = list(map(abc, atcoder))

atmarks = 0
atcoders = 0
for i in range(len(sl)) :
    s, t = sl[i], tl[i]
    if (s == "@") :
        atmarks += 1
    elif s in atcoder :
        atcoders += 1
        sabc[abc(s)] += 1
    else :
        sabc[abc(s)] += 1

    if (t == "@") :
        atmarks += 1
    elif t in atcoder :
        atcoders += 1
        tabc[abc(t)] += 1
    else :
        tabc[abc(t)] += 1

cond = True
for j in range(len(sabc)) :
    if j in atcoderi :
        atcoders -= 2 * (min(sabc[j], tabc[j]))
    else :
        sj, tj = sabc[j], tabc[j]
        if sj != tj :
            cond = False
            break

if atcoders > atmarks :
    cond = False

print('Yes' if cond else 'No')