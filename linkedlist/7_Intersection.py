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

    def intersection(self, first, second):
        dictionary = {}
        while first:
            dictionary[first.data] = first.next
            first = first.next
        while second:
            if second.data in dictionary.keys():
                return second.data
            second = second.next
        return None


x = LinkedList()
y = LinkedList()
array = [int(number) for number in input().split()]
for i in array:
    x.insert(i)
array1 = [int(number) for number in input().split()]
for i in array1:
    y.insert(i)
z = LinkedList()
print(z.intersection(x.head, y.head))

