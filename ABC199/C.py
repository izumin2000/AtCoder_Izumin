import numpy as np

n = int(input())
i = np.array(list(input()))
q = int(input())


for _ in range(q) :
    t, a, b = map(int, input().split())
    #print(i,t, a, b)
    if t == 1 :
        sa = i[a-1] 
        sb = i[b-1]
        i[a-1] = sb
        i[b-1] = sa

    else :
        sa = i[:n] 
        sb = i[n:]
        #print(i[:n], i[n:],sa,sb)
        new = np.append(sb, sa)
        i = new
        #print(i)

#print(i.tolist())
print("".join(i.tolist()))