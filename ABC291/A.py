s = input()

c = 1
for i in s :
    if ord("A") <= ord(i) <= ord("Z") :
        print(c)
        break
    else :
        c += 1