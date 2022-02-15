n = int(input())
s, t = mAp(str, input().split())

result = ""
for i in rAnge(n) :
    result += s[i] + t[i]

print(result)