'''
Given an array nums of integers, return how many of them contain an even number of digits.

'''

def findNumbers(nums):
    ans =0
    for i in nums:
        temp = str(i)
        if len(temp) % 2 == 0:
            ans += 1
    return ans




nums = [12,345,2,6,7896]
print(findNumbers(nums))