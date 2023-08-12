while 1 :
    n = int(input())
    if not n :
        break

    l = list(map(int, input().split()))

    c = 0
    j = l[0]
    k = l[1]
    for i in range(n-2) :
        if (l[i] < l[i + 1]) and (l[i + 1] > l[i + 2]) :
            c += 1
    print(c)
