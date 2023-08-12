def f(x, i = -1, j = -1) :
    if j == 1 :
        return "j"
    if i == 1 :
        return "i"
    else :
        return x
    
print(f(3))
print(f(3, 1))
print(f(3, j=1))
print(f(3, 2, 1))