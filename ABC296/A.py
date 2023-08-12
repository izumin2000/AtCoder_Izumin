n = int(input())
s = input()
cond = True
for i in range(n-1) :
    a, b = s[i], s[i+1]
    if (a == b) :
        cond = False
print('Yes' if cond else 'No')