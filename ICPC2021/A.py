while 1 :
    ls = list(map(int, input().split()))
    if sum(ls) == 0 :
        break
    while 1 :
        if max(ls) == sum(ls) :
            print(max(ls))
            break
        
        setls = set(ls + [0])
        setls.remove(0)
        min_v = min(setls)
        min_i = ls.index(min(setls))
        for i in range(4) :
            if i != min_i :
                posi = ls[i] - min_v
                if posi >= 0 :
                    ls[i] -= min_v
                else :
                    ls[i] = 0
