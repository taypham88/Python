'''

'''

def findFinalValue(nums, original):
    """
    :type nums: List[int]
    :type original: int
    :rtype: int
    """
    nums.sort()
    temp = original
    for i in range(len(nums)):
        if nums[i] == temp:
            temp *= 2
    return temp

# while(original in nums):
#     original = original*2
# return original

nums = [5,3,6,1,12]
original = 3
print(findFinalValue(nums, original))