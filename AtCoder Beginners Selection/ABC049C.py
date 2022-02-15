s = input()[::-1]
while 1 :
    if len(s) > 5 :
        if s[:6] == 'resare' :
            s = s[6:]
            continue
        elif s[:7] == 'remaerd' :
            s = s[7:]
            continue
    if s == '' :
        print("YES")
        break
    elif len(s) < 5 :
        print("NO")
        break
    elif s[:5] == 'esare' :
        s = s[5:]
        continue
    elif s[:5] == 'maerd' :
        s = s[5:]
        continue
    else :
        print("NO")
        break
