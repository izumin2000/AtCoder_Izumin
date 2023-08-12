c = 8
A = "abcdefgh"
for i in range(8) :
    s = input()
    if "*" in s :
        print(A[s.index("*")]+str(c))
    c -= 1