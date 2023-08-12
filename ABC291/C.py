n = int(input())
s = input()

x, y = 0, 0
cond = False
st = set([(0, 0)])
for i in s :
    if i == "R" :
        x += 1
    if i == "L" :
        x -= 1
    if i == "U" :
        y += 1
    if i == "D" :
        y -= 1
    
    if (x, y) in st :
        cond = True
        break
    else :
        st.add((x, y))

print('Yes' if cond else 'No')