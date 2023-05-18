'''Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.'''

s = 'dfasd fasdfsda fasdfsd dfs'

# my solution
# a = word.split()
# print(len(a[-1]))

# Fastest solution
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
i = len(s) - 1

while i >= 0 and s[i] == " ":
    i -= 1

length = 0

while i >= 0 and s[i] != " ":
    length += 1
    i -= 1


print(length)