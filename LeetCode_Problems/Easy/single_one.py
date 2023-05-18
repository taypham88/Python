# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# solution to this is to use XOR. In binary, the XOR will cancel all other numbers that match except the 1 unquie element.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
            print(ans)
        return ans

    
    
obi = Solution()
print(obi.singleNumber([4,1,2,1,2,4,6]))
print(obi.singleNumber([1]))
      
# Solution that was faster:
# This solution uses pop and compares it to two arrays. 
        # l=[]
        # while True:
        #     a=nums.pop(0)
        #     if a not in nums and a not in l:
        #         return a
        #     l.append(a)