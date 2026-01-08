stack=[]
stack.append(10)                                       # peek will give false hope
stack.append(20)
stack.append(30)
#print(stack.pop())
stack.append(40)
stack.append(50)
stack.append(60)
#print(stack.pop(3))
print(stack)
print("Top element is:",stack[len(stack)-1])
