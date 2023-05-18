'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''


def runningSum(nums):
    ans = []
    sum = 0

    for i in nums:
        sum += i
        ans.append(sum)
    return ans

nums = [1,2,3,4]
print(runningSum(nums))

