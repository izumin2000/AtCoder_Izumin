n = int(input())

b = str(bin(n))[2:]
l = len(b)
#print(b, l)
c = 0
spl = ""
for i in b :
    c += 1
    #print(c, i)
    if i == "1" :
        if c == l :
            spl += "A"
            #print("OK")
        else :
            spl += "AB"
    else :
        if c != l :
            spl += "B"

print(spl)