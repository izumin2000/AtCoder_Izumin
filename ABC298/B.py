import numpy as np

n = int(input())
al = []
for i in range(n) :
    al.append(list(map(int, input().split())))
l = []
for i in range(n) :
    l.append(list(map(int, input().split())))

al = np.array(al)
l1 = np.rot90(al)
l2 = np.rot90(l1)
l3 = np.rot90(l2)

l0 = l - al
l1 = l - l1
l2 = l - l2
l3 = l - l3
cond = not(np.any(l0 == -1)) or not(np.any(l1 == -1)) or not(np.any(l2 == -1)) or not(np.any(l3 == -1))
print('Yes' if cond else 'No')
