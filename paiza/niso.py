n = int(input())
m = int(input())
r = ""
w = False
while m > 0 :
    if w :
        if m > n :
            r += "W"*n
        else :
            r += "W"*m
        w = False
    else :
        if m > n :
            r += "R"*n
        else :
            r += "R"*m
        w = True
    m -= n

print(r)