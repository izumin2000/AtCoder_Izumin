x, y = map(int, input().split())
positionL = []
valueL = []
result = ""

for i in range(50) :
    positionL.append(list(map(int, input().split())))

for j in range(50) :
    valueL.append(list(map(int, input().split())))


visited = [positionL[x][y]]
while 1 :
    look = []
    # up
    if (0 <= x < 50) and (0 <= y < 49) :
        if not positionL[x][y + 1] in visited :
            look.append(valueL[x][y + 1])
        else :
            look.append(0)
    else :
        look.append(0)

    # down
    if (0 <= x < 50) and (1 <= y < 50) :
        if not positionL[x][y - 1] in visited :
            look.append(valueL[x][y - 1])
        else :
            look.append(0)
    else :
        look.append(0)
        
    # right
    if (0 <= x < 49) and (0 <= y < 50) :
        if not positionL[x + 1][y] in visited :
            look.append(valueL[x + 1][y])
        else :
            look.append(0)
    else :
        look.append(0)
        
    # left
    if (1 <= x < 50) and (0 <= y < 50) :
        if not positionL[x - 1][y] in visited :
            look.append(valueL[x - 1][y])
        else :
            look.append(0)
    else :
        look.append(0)
    
    if not sum(look) :
        break
    
    maxdirection = look.index(max(look))
    if maxdirection == 0 :
        result += "R"
        visited.append(positionL[x][y + 1])
        y += 1
    elif maxdirection == 1 :
        result += "L"
        visited.append(positionL[x][y - 1])
        y -= 1
    elif maxdirection == 2 :
        result += "D"
        visited.append(positionL[x + 1][y])
        x += 1
    elif maxdirection == 3 :
        result += "U"
        visited.append(positionL[x - 1][y])
        x -= 1

print(result[:-1])