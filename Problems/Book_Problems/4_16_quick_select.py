'''
4-16. Use the partitioning idea of quicksort to give an algorithm that finds the median element of an array of n integers in expected O(n) time.
(Hint: must you look at both sides of the partition?)

Solution
This is a specialized form of finding the kth largest number; in the median scenario, k = n / 2.
A suitable algorithm here is the QuickSelect algorithm: a randomized version of the QuickSort algorithm.
The algorithm is described as thus:
'''

# Python3 program of Quick Select

# Standard partition process of QuickSort().
# It considers the last element as pivot
# and moves all smaller element to left of
# it and greater elements to right
def partition(arr, l, r):

    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i

# finds the kth position (of the sorted array)
# in a given unsorted array i.e this function
# can be used to find both kth largest and
# kth smallest element in the array.
# ASSUMPTION: all elements in arr[] are distinct
def kthpos(arr, l, r, k):

    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return kthpos(arr, l, index - 1, k)

        # Else recur for right subarray
        return kthpos(arr, index + 1, r,
                            k - index + l - 1)
    print("Index out of bound")

# Driver Code
if __name__ == '__main__':
    arr = [ 10, 4, 5, 8, 6, 11, 26, 30]
    print(sorted(arr))
    n = len(arr)
    k = n//2
    print("medium element of array ", end = "")
    print(kthpos(arr, 0, n - 1, k))

