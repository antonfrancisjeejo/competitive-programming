class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete(self):
        current = self.head
        key = self.size // 2
        for i in range(key - 1):
            current = current.next
        current.next = current.next.next

    def printlist(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end=" ")
            else:
                print(current.data)
            current = current.next


x = LinkedList()
size_of_array = int(input())
array = [int(number) for number in input().split()]
for i in array:
    x.insert(i)
x.delete()
x.printlist()
