

def twoOutOfThree(nums1, nums2, nums3):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :rtype: List[int]
    """
    ans = []
    numbers1 = set(nums1)
    numbers2 = set(nums2)
    numbers3 = set(nums3)
    for num in numbers1:
        if num in numbers2:
            ans.append(num)
    for num in numbers2:
        if num in numbers3:
            ans.append(num)
    for num in numbers1:
        if num in numbers3:
            ans.append(num)
    return list(set(ans))


nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
print(twoOutOfThree(nums1, nums2, nums3))