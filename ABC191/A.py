v, s, g, p = map(int, input().split())
if v * s <= p <= v * g :
    print("No")
else :
    print("Yes")