class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if len(self.stack2) == 0:
            if (len(self.stack1) == 0):
                return 'Cannot dequeue because queue is empty'
        while (len(self.stack1) > 0):
            p = self.stack1.pop()
            self.stack2.append(p)
        return self.stack2.pop()


q = Queue()
array = [int(i) for i in input().split()]
for value in array:
    q.enqueue(value)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
