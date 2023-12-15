n = 0
l = 20000
for i in range(l + 1) :
    if not (i % 3) :
        n += i
    elif '3' in list(str(i)) :
        n += i
print(n)