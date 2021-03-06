# H - イニモン

"""
小ポーション：攻撃力を 1 増やす
大ポーション：攻撃力を 2 倍にする
-> 2進数の問題

攻撃力nを2進数に変換して文字列と見立てたとき、
どの順番でポーションを使えば良いのかがわかる！

例) 攻撃力n = 12

12は2進数で1100
文字列"1100"を左から見ていき、以下の操作をする
'0'なら大ポーションを使用する
'1'なら小ポーションの後に大ポーションを使用する
(ただし一番右の文字なら大ポーションは使用しない)

よって
大ポーション, 小ポーション-大ポーション, 小ポーション-大ポーション
の順に使用すれば攻撃力nを12にすることができる


つまり
小ポーションを使用する操作は文字列'1'が表れたときのみ1回使用するので

-> 
攻撃力nを2進数に変換して文字列と見立てたとき、
'1'の登場回数が小ポーションを使用する回数と合致する
"""
print(bin(int(input())).count('1'))