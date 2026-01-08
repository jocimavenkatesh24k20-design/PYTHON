def postfix(exp):
    stack=[]
    val=0
    for i in exp:
        if i.isdigit():
            stack.append(int(i))
        else:
            a=stack.pop()
            b=stack.pop()
            if i=='+':
                stack.append(b+a)
            elif i=='-':
                stack.append(b-a)
            elif i=='*':
                stack.append(b*a)
            elif i=='//':
                stack.append(b//a)
            elif i=='%':
                stack.append(b%a)
        return stack.pop()
exp = '25-3*54*+9-1'                    #type casting 
print(postfix(exp))