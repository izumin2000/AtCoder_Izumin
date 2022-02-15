x = int(input())

year = 0
yen = 100
while 1:
    year += 1
    yen *= 1.01
    yen = int(yen)
    if yen >= x :
        break
print(year)
