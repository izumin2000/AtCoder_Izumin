import math
a, b, h, m = map(int, input().split())
if h > 12 :
    h -= 12
mnt = h * 60 + m
degA = mnt*math.pi/360
degB = m*math.pi/30
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(degA - degB)))