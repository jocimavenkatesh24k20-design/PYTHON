'''
def BalancedParantheses(paran):
    stack = []
    for i in paran:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                return False
            if (i == ')' and stack[-1] != '(') or \
               (i == '}' and stack[-1] != '{') or \
               (i == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return not stack

paran = input("Enter the parentheses string: ")
if(BalancedParantheses(paran)):
    print("The parentheses are balanced")
else:
    print("The parentheses are not balanced")
'''
def BalancedParantheses(paran):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for i in paran:
        if i in '([{':
            stack.append(i)
        elif i in')]}':
            if not stack or stack[-1] != pairs[i]:
                return 0
            stack.pop()
    return stack == []
paran = input("Enter the parentheses string: ")
if(BalancedParantheses(paran)):
    print("The parentheses are balanced")
else:
    print("The parentheses are not balanced")
