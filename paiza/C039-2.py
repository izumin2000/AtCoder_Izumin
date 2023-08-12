s = input()
l = 0
for i in s.split("+") :
    l += i.count("<") * 10 + i.count("/")
print(l)