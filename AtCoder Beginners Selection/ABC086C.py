n = int(input())
data = []
T = 0
X = 0
Y = 0
for _ in range(n) :
    t, x, y = map(int, input().split())
    t -= T
    x -= X
    y -= Y
    data += [[t, x, y]]
    T = t
    X = x
    Y = y
    
def Bool(t, x, y) :
    remainder = t - x - y
    if remainder >= 0 and remainder%2 == 0:
        return True
    else :
        return False

for i in range(n) :
    if not Bool(data[i][0], data[i][1], data[i][2]) :
        print("No")
        break
    if i+1 == n :
        print("Yes")
