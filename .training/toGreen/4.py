n = int(input())
print(sum([max(0, a-10) for a in list(map(int, input().split()))]))