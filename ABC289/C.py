def isbig(a) :
    return n <= a


n, m = map(int, input().split())
l = []
for _ in range(m) :
    _ = int(input())
    a = map(int, input().split())
    l.append(bool(sum(list(map(isbig, a)))))

a = 0
for bit in range(1 << n):
    combination = [] 
    for i in range(n):
        shift_i = 1 << i
        if bit & shift_i > 0:
            combination.append(l[i])
    a += sum(combination)

print(a)