import math

n = int(input())

fact = []
for i in range(1, 11) :
    fact.append(math.factorial(i))

r = []
c = 0
fact = fact[::-1]
d = n
for j in fact :
    c += d//j
    d = d%j
    
print(c)

