'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
'''

def diStringMatch(s):
    ans, lower, upper  = [], 0, len(s)
    for i in s:
        if i == 'I':
            ans.append(lower)
            lower += 1
        else:
            ans.append(upper)
            upper -= 1
    ans.append(upper)
    return ans

s = "DDI"
print(diStringMatch(s))
