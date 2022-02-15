def sigma(n, m) :
    if n < m :
        return n
    return sigma(n-1, m)

print(sigma(10, 1))