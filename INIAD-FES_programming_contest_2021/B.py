# B - 3教科最高得点重視


a = int(input())
b = int(input())
c = int(input())

if (a > b) and (b > c) :        # 教科aが一番、点数が高かったら
    result = a * 2 + b + c
    print(result)

elif (b > c) and (c > a) :      # 教科bが一番、点数が高かったら
    result = a + b * 2 + c
    print(result)

else :       # (c > a) and (a > b) :と同じ。教科cが一番、点数が高かったら
    result = a + b + c * 2
    print(result)