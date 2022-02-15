def Sort(lst) :
    List = []
    for k in lst :
        List += [int(k)]
    List.sort()
    return List

n = int(input())
a= Sort(input().split())
alice = 0
bob = 0
for i in list(range(0, n))[::2] :
    alice += a[i]
for j in list(range(0, n))[1::2] :
    bob += a[j]
print(abs(alice - bob))
