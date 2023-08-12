from collections import defaultdict
d = defaultdict(str)
e = defaultdict(list)

def shift(s) :
    return s[-1] + s[:-1]


n, m = map(int, input().split())
sl = list(input())
cl = list(map(int, input().split()))

i = 0
for s, c in zip(sl, cl) :
    d[c] += s
    e[c].append(i)
    i += 1

for s, c in d.items() :
    d[s] = shift(c)

ans = [""] * n
for k, v in e.items() :
    # print(f"\033[31m{k, v}\033[0m")
    for i, s in zip(v, d[k]) :
        # print(i, s)
        ans[i] = s
print("".join(ans))