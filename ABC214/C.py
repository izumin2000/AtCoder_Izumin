n = int(input())
sl = list(map(int, input().split()))
tl = list(map(int, input().split()))

r = [10**9] * n

for i in range(n) :
    if tl[i] < r[i] :
        for j in range(n) :
            if j == 0 :
                r[i] = tl[i]
            else :
                new = r[(i + j - 1)%n] + sl[(i + j - 1)%n]
                if new < r[(i + j)%n] :
                    r[(i + j)%n] = new

for p in r :
    print(int(p))