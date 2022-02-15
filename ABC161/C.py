x, k = map(int, input().split())
result = x%k
if x < k :
    if x < (k - x) :
        print(x)
    else :
        print(k - x)
else :
    if result == 0 :
        print(0)
    elif k > result :
        print(abs(k - result))
    else :
        print(result)