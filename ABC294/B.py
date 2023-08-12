h, w = map(int, input().split())
for _ in range(h) :
    al = map(int, input().split())
    for a in al :
        if not(a) :
            print(".", end="")
        else :
            print(chr(a+96).upper(), end="")
    print("")