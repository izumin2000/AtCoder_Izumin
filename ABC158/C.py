import sys

a, b = map(int, input().split())

for price in range(1, 1251):
    if int(price * 0.08) == a :
        if int(price * 0.1) == b :
            print(price)
            sys.exit()
print(-1)