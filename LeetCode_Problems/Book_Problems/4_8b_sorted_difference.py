'''
 We are given a set of  containing  real numbers and a real number , and seek
 efficient algorithms to determine whether two elements of  exist whose sum is exactly .
(b) Assume that  is sorted. Give an  algorithm for the problem.
'''

import numpy as np
# linear complexity + linear is linear time if we do binary search this would be much quicker.

def find_match(list, x):
    diff = []
    for i in range(len(list)):
        diff.append(x-list[i])

    for i in range(len(list)):
        if list[i] == diff[i]:
            return [list[i], diff[i]]

    return False


if __name__ == '__main__':
    s1 = np.random.randint(10, size=100).tolist()
    s1.sort()
    print(find_match(s1, 8))