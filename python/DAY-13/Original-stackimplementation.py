class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if len(self.stack) == 5:
            return("Stack Overflow")
        else:
            self.stack.append(item)
            return ("Item pushed successfully", item)

    def pop(self):
        if not self.stack:
            return "Stack Underflow"
        else:
            return self.stack.pop()

    def Top(self):
        if not self.stack:
            return "Stack is empty" 
        else:
            return self.stack[-1]

    def peek(self):
        if not self.stack:
            return "Stack is empty"
        else:
            return self.stack[-1]

my_stack = Stack()                      #stack object              
'''                      
print(my_stack.push(10))
print(my_stack.push(20))
print(my_stack.push(30))
print(my_stack.pop())
print(my_stack.push(40))
print(my_stack.push(50))
print(my_stack.push(60))
  # This should show "Stack Overflow"
print("Current Stack:", my_stack.stack)
print("Top element is:", my_stack.Top())
'''
            #OR
'''
print(my_stack.Top())
item = [10, 20, 30, 40, 50, 60]
for i in item:
    print(my_stack.push(i))
    print(my_stack.stack)
    '''