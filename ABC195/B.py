

a,b,w = map(int, input().split())

x = (w*1000)/b
y = int((w*1000)/a)

if int(x) - x != 0.0 :
    x = int(x) + 1
else :
    x = int(x)

if w*1000//a == w*1000//b :
    print("UNSATISFIABLE")
else :
    print(str(x)+ " " + str(y))