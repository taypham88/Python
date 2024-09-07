"""Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""

class Solution(object):
    def strStr(self, haystack, needle):

        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

"""class Solution(object):
    def strStr(self, haystack, needle):
        d = {needle: 1}
        if len(needle) == 0:
            return 0
        i = 0
        while i + len(needle) <= len(haystack):
            if d.get(haystack[i:i+len(needle)], 0) > 0:
                return i
            i += 1
        return -1"""


obi = Solution()
print(obi.strStr("hello", "ll"))
print(obi.strStr("aaaaa", "bba"))
print(obi.strStr("", ""))
print(obi.strStr("", "a"))
print(obi.strStr("a", "a"))