a,b = map(int, input().split())
c = 0
while 1 :
    if bin(a ^ c) == bin(b) :
        break
    c += 1

print(c)