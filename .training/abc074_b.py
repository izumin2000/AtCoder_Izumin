import numpy as np

n = int(input())
k = int(input())
xl = np.array(list(map(int, input().split())))

al = np.where(xl < k/2, xl * 2, 0)    #Aの方が良い
bl = np.where(xl >= k/2, abs(xl - k)*2, 0)
al = np.append(al, bl)
    
print(np.sum(al))