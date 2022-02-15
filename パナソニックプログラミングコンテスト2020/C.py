import math
a, b, c = map(int, input().split())
l = math.sqrt(a) + math.sqrt(b)
r = math.sqrt(c)
if l*(10**16) < r*(10**16) :
    
    print("Yes")
else :
    print("No")
