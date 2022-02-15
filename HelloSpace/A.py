s = input()
n = 0

while ("ZONe" in s) :
    n += 1
    s = s.replace("ZONe", "", 1)

print(n)