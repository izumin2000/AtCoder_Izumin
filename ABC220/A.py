a, b, c = map(int, input().split())

bl = True
for i in range(1, 11) :
    n = i * c
    if a <= n <= b :
        print(i * c)
        bl = False
        break

if bl :
    print(-1)