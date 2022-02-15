n = int(input())

c = 0
for i in range(1, n + 1) :
    for j in range(1, int(n / i) + 1) :
        for k in range(1, int(n / i / j) + 1) :
            if (i * j * k) <= n :
                c += 1

print(c)