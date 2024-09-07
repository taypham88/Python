'''
Given an integer array nums of length n, you want to create an array ans of
length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
'''

def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return nums + nums

if __name__ == '__main__':
    a =[1,2,1]
    print(getConcatenation(a))
