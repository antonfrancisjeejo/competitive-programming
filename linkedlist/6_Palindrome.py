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
            self.size += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.size += 1

    def reverse(self, start):
        prev = None
        current = start
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def is_palindrome(self):
        current = self.head
        flag = True
        if self.size % 2 == 0:
            mid = self.size // 2
        else:
            mid = (self.size + 1) // 2
        for i in range(1, mid):
            current = current.next
        reverse_head = self.reverse(current.next)
        current = self.head
        while current is not None and reverse_head is not None:
            if current.data != reverse_head.data:
                flag = False
                break
            current = current.next
            reverse_head = reverse_head.next
        if flag:
            print('yes')
        else:
            print('no')


x = LinkedList()
size_of_array = int(input())
array = input().split()
for i in array:
    x.insert(i)
x.is_palindrome()
