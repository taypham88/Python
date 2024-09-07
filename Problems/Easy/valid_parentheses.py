"""class Solution(object):
    def isValid(self, s):
        l = []
        for i in s:
            if i in ['(', '{', '[']:
                l.append(i)
            elif i == ')' and len(l) != 0 and l[-1] == '(':
                l.pop()
            elif i == '}' and len(l) != 0 and l[-1] == '{':
                l.pop()
            elif i == ']' and len(l) != 0 and l[-1] == '[':
                l.pop()
            else:
                return False
        return l == []"""

class Solution(object):
    def isValid(self, s):

        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for p in s:
            print(f"p is {p}")
            print(f"stack before {stack}")
            if p in dic:
                stack.append(dic[p])
                print(f"stack after append {stack}")
            elif p not in dic:
                print(f"stack in elif {stack}")
                if len(stack) == 0 or stack.pop() != p:
                    print("if activated")
                    return False
            print(f"stack after if {stack}")
        if len(stack) == 0:
            return True
        else:
            return False
    
obi = Solution()
#print(obi.isValid("()[]{}"))
#print(obi.isValid("[}()"))
#print(obi.isValid("{()}"))
print(obi.isValid("(((()"))