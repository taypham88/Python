'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.
'''

def arrayStringsAreEqual(word1, word2):
    # phrase1 = "".join(word1)
    # phrase2 = "".join(word2)
    # if phrase1 == phrase2:
    #     return True
    # else:
    #     return False
# one line
    return ''.join(word1) == ''.join(word2)

word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(arrayStringsAreEqual(word1,word2))