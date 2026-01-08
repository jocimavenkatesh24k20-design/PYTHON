def reverse_string(string):
    reverse_string=""
    stack = []

# Input string
string = input("Enter a string: ")

# PUSH each character into stack
for char in string:
    stack.append(char)

# POP characters to reverse string
reversed_string = ""
while len(stack) != 0:
    reversed_string += stack.pop()

print("Reversed string:", reversed_string)