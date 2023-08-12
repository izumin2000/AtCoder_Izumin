import collections
n, m = map(int, input().split())
d = {}
sells = list(map(int, input().split()))
sellc = collections.Counter(sells)
buys = list(map(int, input().split()))
buyc = collections.Counter(buys)

for i in sorted(sells + buys) :
    sell = sellc[i] if i in sellc.keys() else 0
    buy = buyc[i] if i in buyc.keys() else 0
    d[i] = (sell, buy)

print(f"\033[31m{d}\033[0m")
sellc, buyc = 0, 0
for k, v in d.items() :
    sell, buy = v
    sellc += sell
    buyc += buy
    print(f"\033[31m{k, sellc, buyc}\033[0m")
    if sellc == buyc :
        print(k)
        # break
    elif sellc > buyc :
        print(k + 1)
        # break