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

    def print_kth_element_from_last(self, key):
        slow = fast = self.head
        for i in range(key):
            fast = fast.next
        if not fast:
            return slow.next
        while fast != None:
            fast = fast.next
            slow = slow.next
        return slow.data

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
key = int(input())
for i in array:
    x.insert(i)
print(x.print_kth_element_from_last(key))

