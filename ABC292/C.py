import itertools

n = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def solve(l) :
    if (l != [[1, 1]]) :
        a = 1
    elif (len(l) == 1) and (1) :
        a = 2
    else :
        al = []
        for i in l :
            al += i[1]
        a = len(list(itertools.combinations(al, 2)))
        a += 2
    return a

ans = 0
for i in range(1, n) :
    l = factorization(i)
    m = factorization(n - i)
    print(l, m, solve(l), solve(m))
    ans += solve(l) * solve(m)

print(ans)
