n = int(input())
List = []
result = []
for _ in range(0, n) :
    List += [int(input())]

for i in List :
    if not i in result :
        result += [i]
print(len(result))
