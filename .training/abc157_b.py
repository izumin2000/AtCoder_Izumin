import numpy as np

a11, a12, a13 = map(int, input().split())
a21, a22, a23 = map(int, input().split())
a31, a32, a33 = map(int, input().split())
l = np.array([a11, a12, a13, a21, a22, a23, a31, a32 ,a33])
marked = np.array([])

n = int(input())

for i in range(n) :
    drop = int(input())
    ll = np.arange(len(l))[l == drop]
    marked = np.append(marked, ll)

check = np.array([])
check = np.append(check, np.intersect1d(marked, [0, 1, 2 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [3, 4, 5 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [6, 7, 8 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [0, 3, 6 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [1, 4, 7 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [2, 5, 8 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [0, 4, 8 ]).shape[0])
check = np.append(check, np.intersect1d(marked, [2, 4, 6 ]).shape[0])

if np.max(check) == 3 :
    print("Yes")
else :
    print("No")