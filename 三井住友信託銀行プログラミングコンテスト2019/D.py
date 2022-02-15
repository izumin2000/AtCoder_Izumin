n = int(input())
s = input()
lst = []
List = []
result = []

for i in s :
    lst += [i]

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            List += [int(lst[i] + lst[j] + lst[k])]

for i in List :
    if not i in result :
        result += [i]

print(len(result))