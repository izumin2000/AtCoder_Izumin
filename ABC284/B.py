def f(l) :
    return bool(l%2)

n = int(input())

for _ in range(n) :
    a = 0
    m = int(input())
    l = list(map(int, input().split()))
    print(sum(list(map(f, l))))