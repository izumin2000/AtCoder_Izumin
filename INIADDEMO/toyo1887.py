# (a * b) % M <=> (a % M) * (b % M)

l, r = map(int, input().split())

if (r//1887 - l//1887) >= 1 :   # if range r ~ l have a number of multiples of 1887
    print(0)

else :
    n = l%1887
    print(n * (n + 1))