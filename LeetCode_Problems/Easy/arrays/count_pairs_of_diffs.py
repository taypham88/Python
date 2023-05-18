'''
Given an integer array nums and an integer k, return the number of pairs (i, j)
where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
'''

def countKDifference(nums, k):
    lookup = {}
    count = 0
    for i in nums:
        if i not in lookup:
            lookup[i] = 0
        lookup[i] += 1
    print(lookup)
    for i in nums:
        if i+k in nums:
            count += lookup[i+k]
    return count

nums = [1,2,2,1]
k = 1

print(countKDifference(nums, k))
