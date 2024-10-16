"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums."""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
            

    
obi = Solution()
print(obi.removeDuplicates([1,1,2]))
print(obi.removeDuplicates([1,2,3,9,9,4,4,6]))
print(obi.removeDuplicates([1,2,3,4,4,4,4,7]))

"""fastest solution:
    
        i = 1
        while i<= len(nums)-1:
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)"""