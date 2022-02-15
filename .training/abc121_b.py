import numpy as np

n, m, c= map(int, input().split())
bl = np.array(list(map(int, input().split())))
count = 0

for _ in range(n) :
    al = np.array(list(map(int, input().split())))
    x = np.sum(al * bl) + c
    if x > 0 :
        count += 1

print(count)