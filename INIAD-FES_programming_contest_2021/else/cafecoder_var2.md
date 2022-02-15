# top

### コンテストの概要
当サイトにて、初心者でも楽しめる競技プログラミング大会を開催します！学年や学部内外問わず誰でも参加できます。競プロってなに？という人も大歓迎！みなさんのご参加をお待ちしています。

協力:「[CafeCoder](https://cafecoder.top/)」「[Algorithm Caballeros](https://sites.google.com/iniad.org/algorithm-caballeros)」


### コンテスト情報
コンテスト時間: 60 分
誤答ペナルティ: 1 分
writer: izumin, polarity
tester: Lain, ir_1st_vil 

### コンテストルール
コンテスト中の他者との問題や解法共、インターネット上での公開は禁止されています。ご注意ください。
インターネット上のコードを利用したり、インターネットでの検索結果・書籍の情報を参照することは可能です。


### 注意点
コードを提出する際は**提出する言語**が正しいか確認してください。初期状態はC++17 (g++ 10.2.0)になっているため、例えば、pythonで提出したい場合は提出する言語の欄をクリックして、Python (3.9.0)を選択してください。

### 制限について
メモリ制限は 512 MB です。
実行時間制限は問題ページに記載しています。

### 難易度について
当コンテストでは難易度を以下のように表しております。下にいくほど難しくなっております。
|  難易度  |  読み方  |  説明  |
| ---- | ---- |
|  Milk  |  ミルク  |  INIAD生なら簡単に解けるほどの難易度です。  |
|  Assam  |  アッサム  |  定期テストレベルくらいの難易度の問題です。これさえとければCSの成績Sは間違え無しです。  |
|  Benihuki  |  べにふうき  |  競技プログラマーとしての基礎的なアルゴリズムの知識や多少の数学的が必要なほどの難易度の問題です。これが解けると教授に褒めてもらえるでしょう。  |
|  ผักชี   |  パクチー  |  競技プログラマーでは無い人にとっては難しいですが、アルゴリズムの授業を取ったことがある人なら解法がわかるかもしれないくらいの難易度の問題です。これが解けた方は就活でアピールできるレベルのアルゴリズム力の持ち主です。  |


# A - あと何単位必要？
### 日本の大学では124単位以上の単位を取得しないと卒業できません。Enryoさんは現在n単位を取得しています。Enryoさんはあと何単位取得しなくてはいけないでしょうか？

- 入力
n

- 出力
答えを出力してください。

- 制約
0 <= n <= 124
入力は全て整数
---
- 入力例 1
24

- 出力例 1
100

- 解説 1
24単位取得しているので124 - 24単位であと100単位必要です。
---
- 入力例 2
124

- 出力例 2
0

- 解説 2
Koshi君は優秀です。
---
# B - 3教科最高得点重視
### 東洋大学情報連携学部の入試には3教科最高得点重視という3教科の内、最高得点科目の得点を2倍する方式で得点計算が行われます。TANAKAさんはこの入試を受験したところ、各教科の点数はそれぞれa点, b点, c点でした。このとき、3教科最高得点重視での点数はいくらになるでしょうか？ 

- 入力
a
b
c

- 出力
答えを出力してください。

- 制約
0 <= a, b, c <= 100
a, b, cは相異なる
入力は全て整数
---
- 入力例 1
100
90
80

- 出力例 1
370

- 解説 1
最高点は100点なので、100 * 2 + 90 + 90 = 380点になります。
---
- 入力例 2
32
48
70


- 出力例 2
220 
---
# C - INIADINIADINIADINIAD...
### 文字列"INIAD"がn回繰り返す文字列を出力してください。

- 入力
n

- 出力
答えを出力してください。

- 制約
1 <= n <= 124
入力は全て整数
---
- 入力例 1
3

- 出力例 1
INIADINIADINIAD

- 解説 1
"INIADINIADINIAD"は文字列"INIAD"が三回繰り返す文字列です。
---
- 入力例 2
10

- 出力例 2
INIADINIADINIADINIADINIADINIADINIADINIADINIADINIAD
---
# D - INIADAINI
### 文字列sが与えられるので回文かどうか判断して回文ならYes、回文でないのならNoを出力してください。

- 入力
s

- 出力
YesかNoを出力してください。

- 制約
文字列sは英小文字のみからなる
文字列sの文字数は1文字以上100文字未満
---
- 入力例 1
INIADDAINI

- 出力例 1
Yes

- 解説 1
INIADDAINIは回文です。
---
- 入力例 2
python

- 出力例 2
No
---
- 入力例 3
neveroddoreven

- 出力例 3
Yes
---
# E - INDIAN
### 文字列sが与えられます。アルファベット'a', 'd', 'i', 'n'のみからなる文字列のときYesを、そうでないのならNoを出力してください。

- 入力
s

- 出力
YesかNoを出力してください。 

- 制約
文字列sは英小文字のみからなる
文字列sの文字数は1文字以上100文字未満
---
- 入力例 1
ai

- 出力例 1
Yes

- 解説 1
文字列AIはアルファベットのAとIでできています。条件に一致するのでYesを出力してください
---
- 入力例 2
btron

- 出力例 2
No
---
- 入力例 3
indian

- 出力例 3
Yes
---


# F - 密です
### INIADの小教室の円卓の周りにはn個の椅子があります。ある連続する2席に人が座っている状態のことを「密の状態」とします。長さnの文字列が与えられるので密の状態か判断しもしそうならYes、そうでないのならNoを出力してください。

- 入力
s

- 出力
YesかNoを出力してください。 

- 制約
文字列sの文字数は2文字以上100文字以下
sの各文字はoかxである
sのi番目の文字s[i]はi番目の席を表す
s[i]がoのときは人が座っている椅子を表し、xのときは人が座っていない椅子を表す。
---

- 入力例 1
oxooxx

- 出力例 1
Yes

- 解説 1
3番目と4番目の椅子にそれぞれ人が座っていて隣り合っている状態のため、密です。
---
- 入力例 2
oxo

- 出力例 2
Yes 

- 解説 2
1番目と3番目の椅子にそれぞれ人が座っていて隣り合っている状態のため、密です。机は円卓なことを考慮してください。
---
- 入力例 3
oxxxxxxxxxxox

- 出力例 2
No
---
# G - 全休はある？
### INIADでは1限から6限まで月曜日から土曜日まで授業が開講されています。時間割が6文字の文字列が6行分与えられるので、全休があるか判断してあるのならYes、ないのならNoを出力してください。ただし、全休というのは1日中授業が無い日のことを指します。

- 入力
c(1,1)c(1,2) ... c(1,6)
c(2,1)c(2,2) ... c(2,6)
...   ...        ...
c(6,1)c(6,2) ... c(6,6)

- 出力
YesかNoを出力してください。 

- 制約
文字c(i,j)のiはi限目を表していて、jは月曜日を1と、火曜日を2のように数字で土曜日まで表している。
1 <= i, j <= 6
各cにはoかxのいずれかが与えられる。
oは授業がある日を、xは授業が無い日を表す。
---

- 入力例 1
xxxxxx
xoooxx
xooxxx
ooooxx
oxxoxx
xoxxxx

- 出力例 1
Yes

- 解説 1
一番右の列と右から2番目の列、つまり時間割でいう金曜日と土曜日が全部xで全休なのでYesを出力してください
---
- 入力例 2
oxoxox
xoxoxo
oxoxox
xoxoxo
oxoxox
xoxoxo

- 出力例 2
No
---

# H - イニモン
### 東洋大学赤羽台キャンパスにはINIADモンスターが出現します。Kenさんは攻撃力が0のINIADモンスターに対して以下のアイテムを1つ以上使い、攻撃力をちょうどnに増やしたいです。
### 小ポーション：攻撃力を1増やす
### 大ポーション：攻撃力を倍にする
### このとき、Kenさんは最低でも何個の小ポーションが必要でしょうか。必要な数を出力してください。


- 入力
n

- 出力
答えを出力してください。

- 制約
1 <= n <= 10の100乗
入力は全て整数
---
- 入力例 1
12

- 出力例 1
2

- 解説 1
小ポーション, 大ポーション, 小ポーション, 大ポーション, 大ポーションの順にアイテムを消費すると、最小限の小ポーションの消費で攻撃力をちょうど12にすることができます。小ポーションは2個消費するので2を出力してください

---
- 入力例 2
10000000000000

- 出力例 2
14

---
# I - リストにいるenryoさん
### enryoさんは長さn + 1のリストAの0番目にいて0点持っていています。enryoさんは0番目からn番目を目指して移動することにしました。enryoさんがi番目にいるとき、以下の3つの方法で移動することができます。
### Xポイント失ってi + 1に移動します。このときA[i + 1]点獲得します。
### Xポイント失ってi + 1に移動します。このときA[i + 1]点獲得します。
### Zポイント失ってd * i に移動します。このときA[d * i]点獲得します。ただしiは1番目以上でかつ、dは2以上の自然数とします。
### このとき、enryoさんはn番目に到達した時点で最大何点獲得することができますか？

- 入力
n X Y Z
A[1] A[2] ... A[n]

- 出力
答えを出力してください。

- 制約
1 <= n <= 100000
-1000 <= X, Y, Z, A[i] <= 1000
入力は全て整数
---
- 入力例 1
8 1 1 2 
0 0 -1 3 -2 4 3 4

- 出力例 1
9

---
# J - 奇数好きのenryoさん
### enryoさんは奇数が好きです。そこで重複を許すn個の数があるリストAの中から、数を0個以上用いて総和ができるだけ大きな奇数を作ることにしました。総和が最大の数を出力してください。ただし奇数を作ることができない場合は0を出力してください。


- 入力
n
A[1] A[2] ... A[n]

- 出力
答えを出力してください。

- 制約
1 <= n <= 100000
-10000 <= A[i] <= 10000
リストA内に少なくとも1つは奇数である
入力は全て整数
---
- 入力例 1
8
5 4 7 -2 0 5 8 -3 

- 出力例 1
29

- 解説 1
5, 4, 7, 5, 8を選ぶと、最大である総和の29を作ることができます。

---
- 入力例 2
3
2 -1 0

- 出力例 2
1