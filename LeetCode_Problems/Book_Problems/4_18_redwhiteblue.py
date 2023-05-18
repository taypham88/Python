'''
4-18. Suppose an array A consists of n elements, each of which is red, white, or blue. We seek to sort the elements so that all the reds come
before all the whites, which come before all the blues. The only operation permitted on the keys are

Examine(A, i) -- report the color of the ith element of A.
Swap(A, i, j) -- swap the ith element of A with the jth element.
Find a correct and efficient algorithm for red-white-blue sorting. There is a linear-time solution.
'''
import numpy as np
# 1 and 2 could be strings as well.
def dutchsort(arr, n):
    low = 0
    mid = 0
    high = n -1

    while mid <= high:
        if arr[mid] == 'red':
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 'blue':
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
    return arr

# Driver Code
if __name__ == '__main__':
    l =[]
    arr = np.random.randint(3, size=10).tolist()
    for i in arr:
        if i == 0:
            l.append('red')
        elif i==1:
            l.append('blue')
        else:
            l.append('white')
    print(l)
    n = len(l)
    output = dutchsort(l, n)
    print(output)