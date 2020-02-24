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

    def add_two_numbers(self, l1, l2):
        sum_of_lists = l1.data + l2.data
        carry = int(sum_of_lists / 10)
        self.head = Node(sum_of_lists % 10)
        p1 = l1.next
        p2 = l2.next
        p3 = self.head
        while p1 is not None or p2 is not None:
            sum_of_lists = carry + (p1.data if p1 else 0) + (p2.data if p2 else 0)
            carry = int(sum_of_lists / 10)
            p3.next = Node(sum_of_lists % 10)
            p3 = p3.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if carry > 0:
            p3.next = Node(carry)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev


x = LinkedList()
y = LinkedList()
array = [int(number) for number in input().split()]
for i in array:
    x.insert(i)
array1 = [int(number) for number in input().split()]
for i in array1:
    y.insert(i)
x.reverse()
y.reverse()
z = LinkedList()
z.add_two_numbers(x.head, y.head)
z.reverse()
z.printlist()
