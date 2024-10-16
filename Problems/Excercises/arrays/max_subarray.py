

def maxSubArray(nums):
    print(nums)
    mem, curr = 0, 0
    for i in nums:
        curr += i
        print(curr)
        # if mem > curr:
        #     return mem
        # else:
        #     mem = curr
    return curr

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))