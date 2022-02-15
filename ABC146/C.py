a, b, x = map(int, input().split())
def price(a, b, n) :
    return a * n + b * len(str(n))

result = -1
num = 0

if price(a, b, 0) > x :
    print(0)
else :
    for digit in range(0, 10, -1) :
        for num in range(0, 9, -1) :
            if price(a, b, num*digit**10) < x < price(a, b, (num+1)*digit**10) :
                result += num*digit**10
                break
            print(result)
        
"""








        digit = len(str(x))
        while 1 :
            print(result)
            if price(a, b, result) < x :
                result += 10**digit
            else :
                break
"""
