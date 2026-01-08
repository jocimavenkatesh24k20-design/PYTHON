'''
'''
def isvalid(paran):
    count = 0
    for i in paran:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return 0
    return count == 0
paran = input("Enter the parentheses string: ")
if(isvalid(paran)):
    print("The parentheses are valid")
else:
    print("The parentheses are not valid")