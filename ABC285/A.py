l = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13), (7, 14), (7, 15)]

a, b = map(int, input().split())
cond = (a, b) in l
print('Yes' if cond else 'No')