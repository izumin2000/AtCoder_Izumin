from collections import deque
import re
import sys

s = input()
symbols = list(re.sub('[a-z]|[A-Z]|[0-9]', '', s))      # 記号以外を削除
stack = deque()

for symbol in symbols :     # 記号を左からみていく
    if symbol in '[{(' :        # もし、開き括弧なら
        stack.append(symbol)
        
    elif symbol in ']})' :      # もし、閉じ括弧なら
        if not len(stack) :     # stackに何もなかったら（開き括弧より閉じ括弧の方が数が多い場合）
            print('正しくない')
            sys.exit()
        
        if not (stack[-1], symbol) in [('(', ')'), ('[', ']'), ('{', '}')] :        #括弧の種類が対応していない場合は
            print('正しくない')
            sys.exit()
            
        stack.pop()
    
            
print('正しくない' if len(stack) else '正しい')     # 閉じ括弧より開き括弧の方が数が多い場合は'正しくない'を出力。それ以外が'正しい'を出力。

# 解いた感想
# 前にstack・queueが登場する過去問( https://atcoder.jp/contests/abc237/tasks/abc237_d )を解いたことがあるので、懐かしい気持ちになりました。