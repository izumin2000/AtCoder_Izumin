n, x = map(int, input().split())
l = list(map(int, input().split()))
al = [x + a for a in l]
l = set(l) & set(al)
print('Yes' if l else 'No')