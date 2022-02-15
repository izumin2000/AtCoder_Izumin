# D - INIADAINI


s = input()

"""
スライスを使ってみよう！
文字列sはs[::-1]で反転できる

例)
s = "abc"
print(s[::-1])
出力：cba

※ 組み込み関数 reversed()でも同じことができる
"""

if s == s[::-1] :       # 回文なら
    print("Yes")
else :      # 回文でないのなら
    print("No")