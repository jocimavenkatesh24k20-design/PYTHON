from collections import deque
                                            #deque is a list
dq=deque()
dq.append(10)
dq.appendleft(5)                            #it can insert both side of element
dq.insert(1,7.3)                          
print(dq)
dq.popleft()                                 #it access the 1st element
print(dq.pop())                         #it access the last element
dq1.rotate(2)
print(dq1)