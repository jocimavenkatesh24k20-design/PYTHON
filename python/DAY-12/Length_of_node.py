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
def print_list(newnode):
    temp=newnode
    while temp:
        print(temp.data,end=" => ")
        temp=temp.next
print("None\n list is printed")

def length_of_list(newnode):
    count=0
    temp=newnode
    while temp:
        count+=1
        temp=temp.next
    return count

print_list(newnode)
print("\nLength of linked list is:",length_of_list(newnode))