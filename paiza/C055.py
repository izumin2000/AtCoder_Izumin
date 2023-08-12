n = int(input())
g = input()
l = []
for _ in range(n) :
    s = input()
    if g in s :
        l.append(s)

if l :
    print("\n".join(l))
else :
    print("None")
