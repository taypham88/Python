'''
Given two sets S1 and S2 (each of size n), and a number x, describe an O(nlogn) algorithm for
finding whether there exists a pair of elements, one from S1 and one from S2, that add up to x.
(For partial credit, give a Θ(n2) algorithm for this problem.)
'''
import numpy as np

def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return [True, mid]

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return [False, -1]

def s1_s2_problem(s1, s2, x):
    s1.sort()
    for num in s2:
        si = x - num
        if binarySearch(s1, si, 0, len(s1)-1)[0] is True:
            return True, s1[binarySearch(s1, si, 0, len(s1)-1)[1]], num
    return False, -1, -1

if __name__ == '__main__':
    s1 = np.random.randint(20, size=10).tolist()
    s2 = np.random.randint(20, size=10).tolist()
    print(s1_s2_problem(s1,s2, 10))
