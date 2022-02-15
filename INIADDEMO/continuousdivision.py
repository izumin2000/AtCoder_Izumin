n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))[::-1]

mx = 0
absl = []
for i in l :
    if i > 0 :
        mx += i
        absl.append(i)
    else :
        absl.append(-i)

absl = sorted(absl)
print(mx ,absl)
