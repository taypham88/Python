'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ...,
(an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''


def arrayPairSum(nums):
    ans = 0
    nums.sort()
    for i in range(0,len(nums),2):
        ans +=min([nums[i], nums[i+1]])
    return ans

nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))