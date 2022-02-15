while 1 :
    n = int(input())

    if n == 0 :
        break

    l = sorted(list(map(int, input().split())))[::-1]       # sort the inputed list
    result = 0
    
    while 1 :
        print(l)
        while 0 in l :      # delete all 0 
            l.remove(0)
        
        l = sorted(l)[::-1]     # resort l
        if len(l) < 3 :     # if number of color balloon is less than 3. print result
            break
        
        # give 3 balloons for a child and decriment 
        l[0] -= 1
        l[1] -= 1
        l[2] -= 1

        result += 1     # increment