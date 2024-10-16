class Solution(object):
    def longestValidParentheses(self, s):
        l = [(")", -1)]
        ans = 0
        for i in range(len(s)):
            if s[i] == ")" and l[-1][0] == "(": 
                l.pop()
                ans = max(ans, i-l[-1][1])
            else:
                l.append((s[i], i))
        return ans

obi = Solution()
#print(obi.longestValidParentheses("(()"))
#print(obi.longestValidParentheses(")()())"))
#print(obi.longestValidParentheses("(())"))
print(obi.longestValidParentheses("(())()()(((((()))(())()()()"))
 