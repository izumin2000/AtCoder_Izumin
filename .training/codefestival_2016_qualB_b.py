import numpy as np

n, a, b= map(int, input().split())
s = input()
c=0
d=0

for i in s :
    d += 1
    if i =="c" :
        print("No")
    else :
        if i=="a" :
            if c <= a+b :
                print("Yes")
            else :
                print("No")
        else :
            if (c<=a+b) and (d<=b):
                c +=1
                print("Yes")
            else :
                print("No")