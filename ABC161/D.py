import sys
import numpy


k = int(input())

counter = 13
if k < 13 :
    print(k)
else :
    for i in range(13, k**3) :
        counter += 1
        nums = list(map(int, list(str(i))))
        diff = numpy.array(nums[1:]) - numpy.array(nums[:-1])
        if max(diff) > 1 or min(diff) < -1 :
            counter -= 1

        if counter == k :
            print(i+1)
            sys.exit()