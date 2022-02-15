# E - INDIAN

"""
# 
set型を使ってみよう！
set型はpythonの集合を表す型の1つ。
リストとは違い、重複した要素が無く順番が無いのが特徴
set()で文字列に変換できる

例)
xs = set("abcba")
print(xs)

出力: {'a', 'b', 'c'}
※ 順番が無いので出力が異なることがある

"""
s = set(input())
t = set("iniad")        ## t = {'a', 'd', 'i', 'n'}
"""
set型の差集合
ハイフン演算子を使うことで差集合を表すことができる

例)
xs = set("abcd") - set("bdf")

出力: {'a', 'c'}
{'a', 'b', 'c', 'd'} から'b', 'd', 'f'を除外するので'a'と'c'が残る

"""
xs = s - t
if len(xs) == 0 :       # xsが空なら
    print("Yes")
else :
    print("No")