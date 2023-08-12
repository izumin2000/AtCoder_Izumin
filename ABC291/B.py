n = int(input())
x = list(map(int, input().split()))
x = sorted(x)[n:-n]
print(sum(x)/len(x))