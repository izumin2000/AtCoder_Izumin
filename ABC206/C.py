import numpy as np
import math

def f(n) :
    return 0.5 * n * (n-1)

n = int(input())
l = np.array(list(map(int, input().split())))
_, counts = np.unique(l, return_counts=True)

full = f(n)
dup = sum(list(map(f, counts)))

print(int(full - dup))