n, x, t = map(int, input().split())
r = 0
while n > 0 :
    n -= x 
    r += t
print(r)