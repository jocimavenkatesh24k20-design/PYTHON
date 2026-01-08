class node:
    def __init__(self,data):
        self.data=data
        self.next=None

newnode=node(10)
newnode_1=node(20)
newnode_2=node(30)

newnode.next=newnode_1
newnode_1.next=newnode_2

temp=newnode
while temp:
    print(temp.data,end=" => ")
    temp=temp.next

print("None\n list is printed")