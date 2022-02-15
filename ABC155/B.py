import sys

n = int(input())
a = input().split()
Alist = []
for I in a :
    Alist += [int(I)]

for i in Alist :
    if i%2 == 0 :
        if i%3 != 0 and i%5 != 0: 
            print('DENIED')
            sys.exit()
print('APPROVED')
