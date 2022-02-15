n = input()
d = int(len(n)/2)

if int(n[:d] + n[:d]) > int(n) :
    print(int(n[:d]) - 1)
else :
    print(int(n[:d]))
        