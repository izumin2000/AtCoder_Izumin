import numpy as np

n = int(int(input())/2)
dl = np.sort(np.array(list(map(int, input().split()))))  
    
print(dl[n] - dl[n-1])