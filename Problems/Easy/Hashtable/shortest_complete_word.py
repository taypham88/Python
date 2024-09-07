'''
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
'''


def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    ans = []
    new_string = ''.join(x for x in licensePlate.lower() if not x.isdigit()).replace(" ", "")
    for word in words:
        for i in set(new_string):
            if new_string.count(i) > word.count(i):
                break
        else:
            ans.append(word)
    return sorted(ans, key=len)[0] # or min(ans, key=len)

licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]
print(shortestCompletingWord(licensePlate, words))