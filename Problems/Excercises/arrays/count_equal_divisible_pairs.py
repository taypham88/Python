'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
'''

def countPairs(nums, k):
    # n = len(nums)
    # count = 0
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         if nums[i] == nums[j] and (i*j)%k == 0:
    #             count += 1
    # return count
# using a hashtable/dictionary is faster lookup
    res = 0
    idx = dict()
    l = len(nums)
    for i in range(l):
        if not nums[i] in idx:
            idx[nums[i]] = [i]
        else:
            for j in idx[nums[i]]:
                if((i*j) % k == 0):
                    res += 1
            idx[nums[i]].append(i)
    return res


nums = [3,1,2,2,2,1,3]
k = 2
print(countPairs(nums, k))