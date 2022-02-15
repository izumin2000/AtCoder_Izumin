k, n = map(int, input().split())
a = list(map(int, input().split()))

lst = []
for i in range(0, len(a)-1) :
    lst += [a[i + 1] - a[i]]
lst += [k - a[-1] + a[0]]
print(lst)

print(sum(lst) - max(lst))
