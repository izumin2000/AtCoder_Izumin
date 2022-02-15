import sys
s = input()
x = -1
for i in s :
    x += 1
    if x % 2 == 0 :
        if s[x] != "h" :
            print("No")
            sys.exit()
    else :
        if s[x] != "i" :
            print("No")
            sys.exit()

if len(s)%2 != 0 :
    print("No")
    sys.exit() 

print("Yes")