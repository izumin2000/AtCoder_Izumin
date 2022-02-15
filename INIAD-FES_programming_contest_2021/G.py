#  G - 全休はある？

"""
各曜日が全休か判断するリストを用意する。
Trueなら全休、Falseなら全休では無いことを表すとする。
"""
l = [True, True, True, True, True, True]
for _ in range(6) :
    s = input()

    for i in range(6) :
        if s[i] == "o" :        # 授業があった場合
            l[i] = False        # その曜日を全休では無いようにする

"""
全休が1週間のうち、1日でもある状態 -> リストlに一つでもTrueが残っている状態
"""
if True in l :      # リストにTrueがあったら
    print("Yes")
else :
    print("No")