def chain(l) :
    max_chain = 0
    tmp_chain = 1
    for tmp_l in [l, l[::-1]] :
        for i in range(len(tmp_l) - 1) :
            a, b = tmp_l[i], tmp_l[i + 1]
            if (a + 1) == b :
                tmp_chain += 1
                max_chain = max(max_chain, tmp_chain)
            else :
                tmp_chain = 1
    return max_chain

def rot45(field) :
    n = len(field)
    new_field = []
    for i in range(n) :
        l_upper = []
        l_downer = []
        for j in range(n - i) :
            l_upper.append(field[j][i + j])
            l_downer.append(field[i + j][j])
        new_field.append(l_upper)
        new_field.append(l_downer)
    return new_field[1:]

def rot90(field) :
    n = len(field)
    new_field = [[-1] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            new_field[i][j] = field[j][n - 1 - i]
    return new_field

def search(field) :
    max_chain = 0
    for l in field :
        max_chain = max(max_chain, chain(l))
    return max_chain

n = int(input())
field = []
for _ in range(n) :
    l = list(map(int, list(input())))
    field.append(l)

search_list = [field, rot45(field), rot90(field), rot45(rot90(field))]
print(max(list(map(search, search_list))))