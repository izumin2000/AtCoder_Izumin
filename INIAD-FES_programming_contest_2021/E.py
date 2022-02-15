# E - INDIAN

s = input()
result = "Yes"
for c in s :    # 文字列sを前から1字づつ取り出す
    if (c != 'i') and (c != 'n') and (c != 'a') and (c != 'd'):
        # 文字cがiでもnでもaでもdでもなければ、resultをNoにする
        result = "No"

print(result)