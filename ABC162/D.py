from itertools import permutations, combinations,combinations_with_replacement,product
import numpy as np

n = list(range(1, int(input())))
s = input()
lst = np.array(list(permutations(s, 3)), list(permutations(n, 3)))
print(lst)