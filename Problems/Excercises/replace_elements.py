'''
Given an array arr, replace every element in that array with the greatest
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''

def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    max_value =-1
    for i in range(len(arr)-1, -1,-1):
        temp = arr[i]
        arr[i] = max_value
        max_value = max(temp, arr[i])
    return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))