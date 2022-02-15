import math
result = 0
k = int(input())
for a in range(1, k+1) :
    for b in range(1, k+1) :
        if math.gcd(a ,b) == 1 :
            result += k
        else :
            for c in range(1, k+1) :
                result += math.gcd(math.gcd(a ,b), c)
print(result)
