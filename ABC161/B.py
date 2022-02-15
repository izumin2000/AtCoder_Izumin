n, m = map(int, input().split())
alist = sorted(list(map(int, input().split())), reverse=True)

if alist[m - 1]/sum(alist) >= 1/(4*m) :
    print("Yes")

else :
    print("No")