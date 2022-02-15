def Sum(value) :
    count = 0
    for i in str(value) :
        count += int(i)
    return count

result = 0
n, a, b = map(int, input().split())

for j in range(0, n+1) :
    if a <= Sum(j) <= b :
        result += j
print(result)
