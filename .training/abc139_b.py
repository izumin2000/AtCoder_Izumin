a, b= map(int, input().split())
if b == 1:
    print(0)
elif 0 < b <= a :
    print(1)
else :
    b -= 2
    x = (b // (a - 1)) + 1
    print(x)
