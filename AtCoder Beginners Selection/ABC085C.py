result = []
n, y = map(int, input().split())
for i in range(0, n+1) :
    for j in range(0, n-i+1) :
        if y == 10000*i + 5000*j + 1000*(n-i-j) :
            result = [i, j, n-i-j]
if result == [] :
    result = [-1, -1, -1]

print("{} {} {}".format(result[0], result[1], result[2]))
