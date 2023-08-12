import collections

n = int(input())
s = input().split()

c = 0
d = collections.Counter(s)
for k, v in d.items() :
    c += v//2

print(c)