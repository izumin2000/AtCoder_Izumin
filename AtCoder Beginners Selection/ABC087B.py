count = 0
a = int(input())
b = int(input())
c = int(input())
x = int(input())
for A in range(0, a+1) :
    for B in range(0, b+1) :
        for C in range(0, c+1) :
            if 500*A + 100*B + 50*C == x :
                count += 1
print(count)
