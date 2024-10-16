"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums."""

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return nums


obi = Solution()
print(obi.removeElement([1,2,3,4,4,4,4,6], 4))
print(obi.removeElement([1,2,3,9,9,4,4,6], 9))
print(obi.removeElement([1,2,3,4,4,4,4,7], 7))

"""fastest is:
    
for i in range(nums.count(val)):
    nums.remove(val)
return len(nums)"""