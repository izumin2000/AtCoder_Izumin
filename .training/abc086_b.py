import numpy as np

a, b = input().split()
n = int(a+b)**0.5

if int(n) - n == 0 :
    print("Yes")
else :
    print("No")