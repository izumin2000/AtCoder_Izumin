n = int(input())
s = input()
b = True



for i in range(1, n - 1) :
    a = 0
    b = True
    for j in range(0, n - i) :
        if (s[j] != s[j + i]) and b :
            a += 1
        else :
            b = False
            print(a)
            continue
    print(a)

print(int(s[-1] != s[-2]))
