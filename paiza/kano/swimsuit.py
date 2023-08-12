r = 1
for i in range(int(input())) :
    r *= (i + 1)
while r%10 == 0 :
    r //= 10
r = int(str(r)[-9:])
print(r)