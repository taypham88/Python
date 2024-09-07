class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high1 = nums.pop(nums.index(max(nums)))
        high2 = nums.pop(nums.index(max(nums)))
        low1 = nums.pop(nums.index(min(nums)))
        low2 = nums.pop(nums.index(min(nums)))
        return (high1 * high2) - (low1 * low2)


obi = Solution()
print(obi.plusOne([5,6,2,7,4]))
print(obi.plusOne([4,2,5,9,7,4,8]))