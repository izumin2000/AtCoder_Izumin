# B - 3教科最高得点重視


a = int(input())
b = int(input())
c = int(input())

"""
最高得点科目の得点を2倍する、
つまり教科a, b, cを足し合わせた点数にさらに最高点数教科の点数を足し合わせた点数
"""
print(sum([a, b, c]) + max([a, b, c]))