import string

alphabets = string.ascii_uppercase

a = 0
c = 1
for s in input()[::-1] :
    n = alphabets.index(s) + 1
    a += n * c
    c *= 26

print(a)