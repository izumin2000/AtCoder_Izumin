n = int(input())
lst = []
for i in range(50001) :
    lst += [int(i*1.08)]

if n in lst :
    if int(n/1.08)*1.08 == n :
        print(int(n/1.08))
    else :
        print(int(n/1.08)+1)

else :
    print(":(")
