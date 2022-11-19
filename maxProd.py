#Max product of 5  numbers of a list
#input [3,4,6,9,1,2] output 1296
#input [0, 3, 5, 8, 2, 7, 1, -9] output  1680
#input [0, 3, 5, 8, 2, 7, -1, -29] output 8120 (used -1 and -29)

import numpy as np

def maxProd(nums):
    nums.sort()

    a = nums[-5:]
    b = nums[:2]+ nums[-3:]
    c = nums[:5] + [nums[-1]]
    res = max(np.prod(a), np.prod(b), np.prod(c))

    return res
    

    