n, k, m = map(int, input().split())
List = list(input().split(" "))
All = 0
for i in List :
    All += int(i)

if All + k < m * n :
    print(-1)

else :
    remain = m * n - All 
    if remain <= 0 :
        print(0)
    else :
        print(remain)
