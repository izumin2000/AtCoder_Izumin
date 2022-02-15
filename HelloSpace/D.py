s = input()

def rev(l):
    return l[::-1]

new = ""
temp = ""
l = s.split("R")
lbo = l[:-1]
if len(lbo) == 1 :
    ol = list(map(rev, lbo[::]))
elif len(lbo) != 2 :
    ol = list(map(rev, lbo[::2]))
else :
    ol = list(map(rev, lbo[1::2]))
e = ''.join(ol + [l[-1]])
#print(e)
for i in e:
    if temp != i :
        new += i
        temp = i
    else :
        new = new[:-1]
        if len(new) > 0 :
            temp = new[-1]
    #print(new, " ", temp)

print(new)