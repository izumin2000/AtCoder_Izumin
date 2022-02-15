n , k = map(int, input().split())
nusukes = list(range(1, n+1))
for _ in range(k) :
    d = int(input())
    lst = list(map(int, input().split()))
    for i in lst :
        if i in nusukes :
            nusukes.remove(i)
print(len(nusukes))