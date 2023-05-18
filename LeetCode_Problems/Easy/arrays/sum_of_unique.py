

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup, ans = {}, 0
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        for num in lookup:
            if lookup[num] == 1:
                ans += num
        return ans