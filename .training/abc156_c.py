import numpy as np

#, = map(int, input().split())
n = int(input())
l = np.array(list(map(int, input().split())))

m = int(np.mean(l))
n = m + 1

x = np.sum((l - m)**2)
y = np.sum((l - n)**2)
print(min(x,y))