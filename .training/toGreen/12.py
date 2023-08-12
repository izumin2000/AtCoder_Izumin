import sys
a, b, c = map(int, input().split())
iseven = bool(c % 2)

if a == b :
    print("=")
    sys.exit()

if (abs(a) == abs(b)) and not(iseven) :
    print("=")
    sys.exit()

if iseven :
    cond = a > b
else :
    cond = abs(a) > abs(b)

print('>' if cond else '<')