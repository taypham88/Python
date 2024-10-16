'''

'''

def divideArray(nums):
    s_num = set(nums)
    for i in s_num:
        if nums.count(i) % 2 != 0:
            return False
    return True

nums = [3,2,3,2,2,2]
print( divideArray(nums))