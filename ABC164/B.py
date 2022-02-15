import sys
a, b, c, d = map(int, input().split())
times = (a//d) + 1
if  d >= a :
    if b >= c :
        print("Yes")
        sys.exit()
    else :
        print("No")
        sys.exit()
if a%d == 0 :
    times -= 1
if times * b >= c :
    print("Yes")
else :
    print("No")
