class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def circle_insert(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.head.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=new_node
            new_node.next=self.head
    def printlist(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
            if current==self.head:
                break
    def hasloop(self):
        current=self.head
        loop=0
        while current:
            current=current.next
            if current==self.head:
                loop=1
                break
        if loop==0:
            return False
        else:
            return True
c=CircularLinkedList()
l=CircularLinkedList()
a=int(input())
b=int(input())
for i in range(a,b+1):
    c.circle_insert(i)
for i in range(a,b+1):
    l.insert(i)
if c.hasloop():
    print('It has a loop')
else:
    print("It doesn't has a loop")
if l.hasloop():
    print('It has a loop')
else:
    print("It doesn't has a loop")