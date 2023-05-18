'''
Take a list of  real numbers as input. Design an  algorithm that partitions the numbers into  pairs,
with the property that the partition minimizes the maximum sum of a pair. For example, say we are given the numbers (1,3,5,9).
The possible partitions are ((1,3),(5,9)), ((1,5),(3,9)), and ((1,9),(3,5)). The pair sums for these partitions are (4,14), (6,12), and (10,8).
Thus, the third partition has 10 as its maximum sum, which is the minimum over the three partitions.
'''
# don't really get this question... how can it be the minium over the three partition when its the largest number?

import numpy as np

def min_sum_sort(x):
    x.sort()
    first = [(x[0] + x[1]) , (x[2] + x[3])]
    second = [(x[0] + x[2]), (x[1] + x[3])]
    third = [(x[0] + x[3]) , (x[1] + x[2])]
    return [first, second, third]


y = np.random.randint(100, size=20).tolist()
p = min_sum_sort(y)
print(y)
print(p)

