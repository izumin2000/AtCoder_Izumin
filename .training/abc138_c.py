import numpy as np

n = int(input())
l = sorted(list(map(int, input().split())))
v = l[0]

for i in range(1, n) :
    v = (v + l[i])/2
    
print(v)