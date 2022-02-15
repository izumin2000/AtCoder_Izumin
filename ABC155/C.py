n = int(input())
lst = []
dic = {}
for _ in range(n) :
    s = input()
    lst += [s]

for i in lst :
    if i in dic.keys() :
        dic[i] += 1
    else :
        dic[i] = 1

dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
result = [dic[0][0]]
if len(dic) > 1 :
    for j in range(n-1) :
        if dic[j][1] == dic[j+1][1] :
            result += [dic[j+1][0]]
        else :
            break

result = sorted(result)
for k in result :
    print(k)
