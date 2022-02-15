s, t = map(int, input().split())
r = 0
for i in range(101) :
    for j in range(101) :
        for k in range(101) :
            if (i+j+k) <= s :
                if (i*j*k) <= t :
                    r += 1

print(r)