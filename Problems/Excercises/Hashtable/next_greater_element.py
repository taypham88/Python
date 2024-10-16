'''
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''
def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    greater_hash ={}
    stack, ans =[], []

    for num in nums2:

        while stack and stack[-1] < num:
            greater_hash[stack.pop()] = num
        stack.append(num)
    for item in stack:
        greater_hash[item] = -1
    for num in nums1:
        ans.append(greater_hash[num])
    return ans

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))