'''
Given an integer array nums, move all the even integers at the beginning of the array followed by
all the odd integers.

Return any array that satisfies this condition.

'''

def sortArrayByParity(nums):
    odd, even = [], []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd

nums = [1,0]
print(sortArrayByParity(nums))