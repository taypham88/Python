'''
4.33 Suppose that you are given a sorted sequence of distinct integers {a1, a2, … ,an}.
Give an O(lgn) algorithm to determine whether there exists an i index such as ai=i. For example, in
{-10,-3,3,5,7}, a3=3. In {2,3,4,5,6,7}, there is no such i.
'''

# note this works for lists/arrays but starting with a set and changing it will change its order.

def index_search(array):
    low =0
    high = len(array)

    while low <= high:
        mid = low + high//2

        if array[mid] == mid:

            return True, mid

        if array[mid] > mid:
            high = mid
        else:
            low = mid
    return False, -1

if __name__ == '__main__':
    a = [3,1,2,5]
    # b = sorted(a, key=a.index)
    # print(b)
    print(index_search(a))