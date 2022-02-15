n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
dict = {}
at = 1
amari = 0
loop = 0
dict[1] = 1

while 1 :
    at = lst[at - 1]
    if at in dict.keys() :
        dict[at] += 1
    else :
        dict[at] = 1
    if max(dict.values()) == 1:
        amari += 1
    if max(dict.values()) == 2:
        ans += [at]
        loop += 1
    if max(dict.values()) == 3:
        break

value = (k - amari) % loop
print(lst[value])
