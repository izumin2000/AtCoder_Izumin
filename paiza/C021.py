cx, cy, r1, r2 = map(int, input().split())
n = int(input())
for _ in range(n) :
    nx, ny = map(int, input().split())
    nx, ny = nx - cx, ny - cy
    nr = (nx**2 + ny**2)**0.5
    if r1 <= nr <= r2 :
        print("yes")
    else :
        print("no")