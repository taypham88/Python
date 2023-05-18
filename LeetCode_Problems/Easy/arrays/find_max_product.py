'''
Given the array of integers nums, you will choose two different indices
i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''

def maxProduct(nums):

    nums.sort()
    # x = nums.pop(-1)
    # y = nums.pop(-1)
    return (nums[-1]-1)*(nums[-2]-1)

nums = [3,4,5,2]
print(maxProduct(nums))