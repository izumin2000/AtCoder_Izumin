a = list(input())
r = ""
for i in a :
    if i != "." :
        r += i
    else :
        break

print(int(r))