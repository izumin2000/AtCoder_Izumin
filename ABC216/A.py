l = input().split(".")
x = l[0]
y = int(l[1])
if 0 <= y <= 2 :
    s = "-"
elif 3 <= y <= 6 :
    s = ""
else :
    s = "+"

print(str(x) + s)
