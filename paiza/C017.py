a, b = map(int, input().split())
n = int(input())
for i in range(n) :
    an, bn = map(int, input().split())
    if a > an :
        print("High")
    elif a < an :
        print("Low")
    else :
        if b > bn :
            print("Low")
        elif b < bn :
            print("High")