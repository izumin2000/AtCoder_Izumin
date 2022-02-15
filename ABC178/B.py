a, b, c, d = map(int, input().split())      # 入力
print(max([a*c, a*d, b*c, b*d]))    # 2つの最大、最小をそれぞれ掛け合わせ、その中の最大値を出力する