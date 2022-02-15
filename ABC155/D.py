n, k = map(int, input().split())
A = input().split()
Alist = []
for i in A :
    Alist += [int(i)] 

print(Alist)
result = []
count = 1
for j in Alist :
    for k in Alist[count:] :
        result += [j*k]
    count += 1

ans = sorted(result)
print(ans[1-k])