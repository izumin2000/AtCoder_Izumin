n = int(input())
f = 0
a = 0
for i in range(n) :
    s = input()
    if "For" == s :
        f += 1
    else :
        a += 1

cond = f > a
print('Yes' if cond else 'No')