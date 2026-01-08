class node:
    def __init__(self,data):
        self.data=data
        self.next=None

newnode=node(10)
newnode_1=node(20)
newnode_2=node(30)

newnode.next=newnode_1
newnode_1.next=newnode_2

print(newnode.data,end=" => ")
print(newnode.next.data,end=" => ")
print(newnode.next.next.data,end=" => ")
print("None")
