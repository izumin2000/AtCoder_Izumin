while 1:
    n = int(input())
    if not n :
        break
    l = list(map(int, input().split()))

    print(max(l))