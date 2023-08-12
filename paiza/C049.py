n = int(input())
fb = 1
l = 0
for _ in range(n) :
    fn = int(input())
    l += abs(fn - fb)
    fb = fn
print(l)
