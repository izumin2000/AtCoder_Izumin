import sys
x = int(input())

item = int(x / 105) + 2

for a in range(item) :
    for b in range(item - a) :
        for c in range(item - a - b) :
            for d in range(item - a - b - c) :
                for e in range(item - a - b - c - d) :
                    for f in range(item - a - b - c - d -e) :
                        if 100*a + 101*b  + 102*c + 103*d + 104*e + 105*f == x :
                            print("1")
                            sys.exit()
print("0")
