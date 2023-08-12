n = int(input())
m1 = int(input())
l1 = input().split()
m2 = int(input())
l2 = input().split()
r = []
for i in range(1, n+1) :
    if (not(str(i) in l1)) and (str(i) in l2) :
        r.append(i)

if r == [] :
    print("None")
else :
    print(' '.join([str(a) for a in r]))
    
