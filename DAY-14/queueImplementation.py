class Queue:
    def __init__(self):
        self.Queue = []

    def enqueue(self, item):                            #PUSH = ENQUEUE IN QUEUE      
        if len(self.Queue) == 5:
            return("Queue Overflow")
        else:
            self.Queue.append(item)
            return ("Item pushed successfully", item)

    def dequeue(self):                                  #POP = DEQUEUE IN QUEUE
        if not self.Queue:
            return "Queue Underflow"
        else:
            return self.Queue.pop(0)

    def Top(self):
        if not self.Queue:
            return "Queue is empty"
        else:
            return self.Queue[-1]

    def peek(self):
        if not self.Queue:
            return "Queue is empty"
        else:
            return self.Queue[-1]
        
my_Queue = Queue()                         #Queue object
        
print(my_Queue.Top())
item = [10, 20, 30, 40, 50, 60]
for i in item:
    print(my_Queue.enqueue(i))
    print(my_Queue.Queue)
print(my_Queue.dequeue())
print(my_Queue.enqueue(item[-2]))
print(my_Queue.Queue)