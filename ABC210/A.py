n,a,x,y = map(int, input().split())

if n > a :
    print(a * x + y * (n - a))
else :
    print(n*x)