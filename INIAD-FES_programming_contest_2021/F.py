# F - 密です


s = input()

if (s[0] == 'o') and (s[-1] == 'o') :     # 文字列の端っこ同士はoなら
    print("Yes")
else :
    """
    .count()で文字列の出現個数をカウントしてみよう！
    密な状態 -> 文字列sの中に"oo"がある
    """
    Mitsus = s.count("oo")      # 密の状態になっている箇所の個数

    if Mitsus >= 1 :        # 1つでも密の場所があれば
        print("Yes")
    else :
        print("No")