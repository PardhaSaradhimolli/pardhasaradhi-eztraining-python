class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertbeg(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("empty list")
        else :
            temp=self.head
            while temp:
                print(temp.data,"<->",end=" ")
                temp=temp.next
obj=dll()
n1=Node(10)
obj.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n2
n3.prev=n2
obj.display()
obj.insertbeg()
obj.display()
