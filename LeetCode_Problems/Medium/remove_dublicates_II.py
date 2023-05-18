class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2
        while i<= len(nums)-1:
            if nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)