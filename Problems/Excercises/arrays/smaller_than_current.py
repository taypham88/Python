'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
'''

def smallerNumbersThanCurrent(nums):
    # s_num = sorted(nums)
    # ans = []
    # for i in nums:
    #     count = 0
    #     for j in s_num:
    #         if i > j:
    #             count += 1
    #         else:
    #             break
    #     ans.append(count)
    # return ans
# Quicker thing to do is just to append the index which would be how far up the count it.
    ans = []
    s_num = sorted(nums)
    for i in nums:
        ans.append(s_num.index(i))
    return ans


a = [8,1,2,2,3]
print(smallerNumbersThanCurrent(a))