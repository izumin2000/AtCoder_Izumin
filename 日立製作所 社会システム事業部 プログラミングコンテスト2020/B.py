a, b, m = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

List = [min(aList) + min(bList)]

for _ in range(0, m) :
    x, y, c = map(int, input().split())
    List += [aList[x-1] + bList[y-1] - c]

print(min(List))