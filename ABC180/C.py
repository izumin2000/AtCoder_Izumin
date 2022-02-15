n = int(input())
for i in list(range(n+1, 0, -1)) :
    if (n/i - int(n/i)) == 0 :
        print(int(n/i))
