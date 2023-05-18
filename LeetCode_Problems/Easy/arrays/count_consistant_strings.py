'''
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''
# for else loop is something new i learned
def countConsistentStrings(allowed, words):
    ans = 0
    for word in words:
        for letter in word:
            if letter not in allowed:
                break
        else:
            ans += 1
    return ans
    # count = len(words)
    # for word in words:
    #     for letter in word:
    #         if letter not in allowed:
    #             count -= 1
    #             break
    # return count

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed,words))