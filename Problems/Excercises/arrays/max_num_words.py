'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence.
'''

def mostWordsFound(sentences):
    ans =[]
    for i in sentences:
        ans.append(i.count(" "))
    return max(ans) + 1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))