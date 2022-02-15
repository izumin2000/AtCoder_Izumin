s = input()
r = ""
for i in s[::-1]:
    if i=='1' :
        r += "1"
    elif i == "0" :
        r += "0"
    elif i == "6" :
        r += "9"
    elif i == "8" :
        r += "8"
    elif i == "9" :
        r += "6"
print(r)