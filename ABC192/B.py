s = input()
x = 0
a = ord("a")
b = ord("z")
la = ord("A")
lb = ord("Z")
bol = True

for i in s :
    if x%2 == 0 :
        if la <= ord(i) <= lb :
            bol = False
    else :
        if a <= ord(i) <= b :
            bol = False
    x += 1

if bol :
    print("Yes")
else :
    print("No")