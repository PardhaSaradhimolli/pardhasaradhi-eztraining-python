class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty list")
        else :
            temp=self.head
            while temp:
                print(temp.data,"<->",end=" ")
                temp=temp.next
obj=dll()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n1.prev=n
n2=Node(30)
n1.next=n2
n2.prev=n1
obj.display()
