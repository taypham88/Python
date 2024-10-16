'''
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''

# return sum(c * (c - 1) // 2 for c in Counter(nums).values())

def numIdenticalPairs(nums):
    count = {}

    for i in nums:
        if count.get(i) is None:
            count[i] = 1
        else:
            count[i] = count[i] + 1
    return sum(n * (n-1) //2 for n in count.values())

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))
