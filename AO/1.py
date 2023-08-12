def isShiritori(xs) :
    heads = []
    for x in xs :
        heads.append(x[0])
    teils = []
    for x in xs :
        teils.append(x[-1])
    if "ん" in teils :
        return False
    print(heads, teils)
    if heads[1:] == teils[:-1] :
        return True
    else :
        return False
print(isShiritori(["りんご","ごうかく","くも","もじれつ","つき"]))