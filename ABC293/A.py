s = input()

t = ""
for i in range(1, int(len(s)/2)+1) :
    x = s[2*i-2]
    y = s[2*i-1]
    t += y
    t += x

print(t)