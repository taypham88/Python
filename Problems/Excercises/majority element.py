# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [[x,nums.count(x)] for x in set(nums)]
        
        for i in l:
            if i[-1] > len(nums)/2:
                return i[0]
        



obi = Solution()
print(obi.majorityElement([]))

# if you sort, but is slower:
#             nums.sort()
#         return nums[len(nums)//2]