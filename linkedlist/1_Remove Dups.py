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

    def remove_duplicates(self):
        current = self.head
        previous = None
        duplicate_values = []
        while current:
            if current.data in duplicate_values:
                previous.next = current.next
            else:
                duplicate_values.append(current.data)
                previous = current
            current = current.next

    def printlist(self):
        current = self.head
        while current:
            if current.next is not None:
                print(current.data, end=" ")
            else:
                print(current.data)
            current = current.next


x = LinkedList()
size_of_array = int(input())
array = [int(number) for number in input().split()]
for i in array:
    x.insert(i)
x.remove_duplicates()
x.printlist()
