n = int(input())
p = input().split(" ")
q = input().split(" ")

def fact(n) :
    result = 1
    for i in range(1, n+1) :
        result += i
    return result

def order(n, list) :
    