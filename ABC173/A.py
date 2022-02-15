n = input()
p = int(n[-3:])
if p == 0 :
    print(0)
else :
    print(1000 - int(n[-3:]))