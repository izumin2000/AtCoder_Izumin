s = input()
q = int(input())
qlist = []
for _ in range(0, q) :
    qlist += [input()]

for txt in qlist :
    print(s)
    if len(txt.split()) == 1 :
        s = s[::-1]
    else :
        print(txt.split()[1])
        if txt.split()[1] == 2:
            s = txt.split()[2] + s
        else :
            s += txt.split()[2]
print()
print(s)
