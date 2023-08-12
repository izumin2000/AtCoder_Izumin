n = int(input())
wl = list(map(str, input().split()))
l = ["and", "not", "that", "the", "you"]
cond = False
for i in wl :
    if i in l :
        cond = True
        break

print('Yes' if cond else 'No')