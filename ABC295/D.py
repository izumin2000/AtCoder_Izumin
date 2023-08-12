s = input()
c = 0
for i in range(5*10**5+1) :
    if (str(i)*2) in s:
        c += 1
print(c)