n = input()
d = int(len(n)/2)

#print(int(n[:d]), int("9"*d))

if d == 1 :
    print(int(n[:d]))
else :
    print(int("9"*(d-1))+int(n[:d])-(10**(d-1)))
        