# I - 奇数好きのEnryoさん

"""
考え方)

1. 正の整数を全て足した数を導く
2. その数が奇数なら: 
    答えになるのでそれを出力
3. その数が偶数なら以下の操作をする :
    n = 全て足した数に対して最大の負の奇数を1つ加える
    m = 全て足した数に対して加えた奇数の中で一番小さな偶数を除外する
4. nとmのうち大きい方を出力する

"""
n = int(input())
a = list(map(int, input().split()))
total = 0
positive_odd = 100000       # 最小の正の奇数を記録する変数
negative_odd = -100000      # 最大の負の奇数を記録する変数
 
for u in a:
    if u > 0:       # 正の整数なら
        total += u      # 合計値に加える
 
    if u % 2 == 1:      # 奇数なら
        if u > 0:       # 正の整数なら
            positive_odd = min(positive_odd, u)     # より小さい正の整数に更新
        else:       # 負の整数なら
            negative_odd = max(negative_odd, u)     # より大きい負の整数に更新
 
if total % 2 == 0:      # 偶数なら
    total = max(total + negative_odd, total - positive_odd)     # 大きい2つの操作結果のうち大きい方を選ぶ
 
print(total)