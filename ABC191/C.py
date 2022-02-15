import numpy as np
import math

x, y, r = map(float, input().split())
a = 0

for i in range(int(x-r), int(x+r) + 1, 1) :
    if math.pow(r, 2) - math.pow(i, 2) < 0 :
        continue
    a += int(math.sqrt(math.pow(r, 2) - math.pow(i, 2)) + y) * 2 + 1
    print(int(math.sqrt(math.pow(r, 2) - math.pow(i, 2)) + y) * 2 + 1)

print(a)
