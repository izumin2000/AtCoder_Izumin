s = input().replace("-", "")
l = 0
for i in s :
    i = int(i)
    if i :
        l += i + 2
    else :
        l += 12
print(l * 2)