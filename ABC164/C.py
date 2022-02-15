n = int(input())
result = []
for _ in range(n) :
    thing = input()
    if not thing in result :
        result += [thing]
print(len(result))