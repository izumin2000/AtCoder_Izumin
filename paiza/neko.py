l = [0, 0, 0]
for i in input() :
    if i == "c" :
        l[0] += 1
    elif i == "a" :
        l[1] += 1
    elif i == "t" :
        l[2] += 1

print(min(l))
print(max(l) - l[0])
print(max(l) - l[1])
print(max(l) - l[2])