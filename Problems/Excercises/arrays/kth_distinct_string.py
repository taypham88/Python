'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
'''

def kthDistinct(arr, k):
    """
    :type arr: List[str]
    :type k: int
    :rtype: str
    """
    word_count = {}
    for word  in arr:
        if word  not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    count = 1
    for word in arr:
        if word  in word_count and word_count[word] == 1:
            if count == k:
                return word
            count += 1
    return ""

arr = ["d","b","c","b","c","a"]
k = 2
print(kthDistinct(arr, k))

