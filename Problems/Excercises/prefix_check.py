'''
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.
'''

def countPrefixes(words, s):
    """
    :type words: List[str]
    :type s: str
    :rtype: int
    """
    count = 0
    for word in words:
        if word in s and word == s[:len(word)]:
            count +=1
    return count

words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(countPrefixes(words, s))