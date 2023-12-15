l = [1, 0, 5] + [0] * 30
for i in range(30) :
    l[i + 3] = l[i] + l[i + 1] + l[i + 2]

print(l[30 - 1])