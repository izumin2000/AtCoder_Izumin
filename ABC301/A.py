_ = int(input())
s = input()

if s.count("T") == s.count("A") :
    cond = s[-1] == "A"
    print('T' if cond else 'A')
else :
    cond = s.count("T") > s.count("A")
    print('T' if cond else 'A')