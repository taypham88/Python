'''
A sentence is a list of words that are separated by a single space with no leading or
trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).
'''

def truncateSentence(s, k):
    sentence = s.split()
    ans = []
    for i in range(k):
        ans.append(sentence[i])
    return ' '.join(ans)


s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s,k))