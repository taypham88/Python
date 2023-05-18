#W rite a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 0
        # while n:
        #     print(n)
        #     res += n % 2
        #     n = n >> 1
        # return res
        return str(bin(n)).count('1')


n = 323342
obi = Solution()
print(obi.hammingWeight(n))

