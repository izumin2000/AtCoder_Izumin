n = int(input())
l = [0, 0, 0, 0]
for _ in range(n) :
    s = input()
    if s == "AC" :
        l[0] += 1
    if s == "WA" :
        l[1] += 1
    if s == "TLE" :
        l[2] += 1
    if s == "RE" :
        l[3] += 1
print("AC x " + str(l[0]) + "\nWA x " + str(l[1]) + "\nTLE x " + str(l[2]) + "\nRE x " + str(l[3]))