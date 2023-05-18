'''
Find the balance parentheses. return the position of the first offending parentheses.
'''

def parentheses_balance(s):

    stack =[]
    if s[0] == ')':
        return False, 0

    for i in range(len(s)):
        print(f'i is {i}, s is {s[i]}')
        if s[i] == '(':
            stack.append(i)
            print(stack)
        if s[i] == ')':
            if not stack:
                return False, i
            else:
                stack.pop()
                print(stack)
    if not stack:
        return True
    else:
        return False, stack[0]

print(parentheses_balance("()()())()"))

