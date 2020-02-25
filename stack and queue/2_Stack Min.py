class Stack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0:
            self.min.append(value)
        else:
            if value < self.min[-1]:
                self.min.append(value)
            else:
                self.min.append(self.min[-1])

    def pop(self):
        self.stack.pop()
        self.min.pop()

    def getmin(self):
        return self.min[-1]


s = Stack()
array = [int(i) for i in input().split()]
for value in array:
    s.push(value)
print(s.getmin())
s.pop()
s.pop()
print(s.getmin())
