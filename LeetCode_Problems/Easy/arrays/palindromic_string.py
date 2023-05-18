'''
Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
'''


def firstPalindrome(words):
    for word in words:
        if (word == word[::-1]):
            return word
    return ""


words = ["ujvoejixvaioikkwzxgtmkchckrigfejjpheiiehpjjefgirkchckmtgxzwkkioiavxijeovju"]
print(firstPalindrome(words))