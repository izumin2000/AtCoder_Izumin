"""
a, b = map(int, input().split())
if (a * 6) >= b and (a <= b) :
    print("Yes")
else :
    print("No")
"""
a, b = map(int, input().split())
cond = (a * 6) >= b and (a <= b)
print("Yes" if cond else "No")
