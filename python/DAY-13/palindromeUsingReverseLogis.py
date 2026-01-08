from inspect import stack


string = input("Enter a string: ")
revstr = ""
stack = []
for i in string:
    stack.append(i)

while stack:
    revstr += stack.pop()
print(string,revstr)
if(string==revstr):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#one liner palindrome checker

    print("palindrome" if (string==string[::-1])else"not palindrome")