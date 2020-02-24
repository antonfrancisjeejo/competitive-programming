class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def printlist(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next

    def partition(self, head, x):
        current = head
        before = Node(0)
        after = Node(0)
        before_head = before
        after_head = after
        while current:
            if current.data < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
            after.next = None
        before.next = after_head.next
        self.head = before_head.next


x = LinkedList()
y = LinkedList()
array = [int(number) for number in input().split()]
partition_value = int(input())
for i in array:
    x.insert(i)
x.partition(x.head, partition_value)
x.printlist()


