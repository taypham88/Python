'''
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
A subarray is a contiguous subsequence of the array.
'''

def sumOddLengthSubarrays(arr):
    # if len(arr)== 0:
    #     return 0
    # if len(arr) == 1:
    #     return 1
    # ans = 0
    # for i in range(1,len(arr)+1):
    #     if i%2 ==1:
    #         for x in range(0, len(arr)):
    #             if x+i <= len(arr):
    #                 ans += sum(arr[x:x+i])
    # return ans
# This algo can predict how often that number is called in an odd arrangement.
# The value in the middle happens the most.
# Size of array
    l = len(arr)
    Sum = 0

# Traverse the given array arr[]
    for i in range(l):

    # Add to the sum for each
    # contribution of the arr[i]
        print(((i + 1) *
                (l - i) +
                1) // 2, i+1, l-i)
        Sum += ((((i + 1) *
                (l - i) +
                1) // 2) * arr[i])

# Return the final sum
    return Sum

arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))
