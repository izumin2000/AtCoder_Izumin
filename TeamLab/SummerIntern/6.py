s = set()

for i in range(31) :
    for j in range(41) :
        for k in range(41) :
            n = (205 * i) + (82 * j) + (30 * k)
            s.add(n)
s.remove(0)
print(len(s))
    