a,b,c = map(int, input().split())

if ((a > 0) and (b > 0)) or (c%2 == 0) :
    if abs(a) > abs(b) :
        print(">")
    elif abs(a) < abs(b) :
        print("<")
    else :
        print("=")

else :
    if (a > 0) and (b < 0):
        print(">")
    elif (a < 0) and (b > 0):
        print("<")
    elif (a < 0) and (b < 0):
        if a < b :
            print("<")
        elif a > b :
            print(">")
        else :
            print("=")
    elif (a == 0) and (b < 0) :
        print(">")
    elif (a == 0) and (b > 0) :
        print("<")
    elif (a < 0) and (b == 0) :
        print("<")
    elif (a > 0) and (b == 0) :
        print(">")
    else :
        print("=")