def OddCheck(lst) :
    List = []
    for i in lst :
        if (int(i)%2) == 1 :
            return [False, -1]
        else :
            List += [int(i)/2]
    return [True, List]

counter = 0
List = []

n = int(input())
a = input().split()

while 1:
    if OddCheck(a)[0] :
        counter += 1
        a = OddCheck(a)[1]
    else :
        break

print(counter)
