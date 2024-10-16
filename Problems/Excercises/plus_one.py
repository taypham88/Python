class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        strlist = [str(i) for i in digits]
        num = ''.join(strlist)
        num = int(num) + 1
        digits = [int(i) for i in str(num)]
        return digits
    
# Fastest Answer
    # digits = list(str(int("".join(map(str, digits))) + 1))
    # return digits
    
obi = Solution()
print(obi.plusOne([9,9]))
print(obi.plusOne([2,3,4]))
print(obi.plusOne([9]))
