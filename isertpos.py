class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init(self):
        self.head=None
    def insertposition(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
            n.next=temp.next
            temp.next=n
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before insetion ")
obj.display()
print("")
print("after insertion")
obj.insertposition(2,100)
obj.display()
