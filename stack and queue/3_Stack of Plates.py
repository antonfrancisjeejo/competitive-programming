class Stack:
    def __init__(self, value):
        self.stack = []
        self.sub_stack = []
        self.capacity = value
        self.i = len(self.stack) - 1
        self.count = 0

    def push(self, value):
        if len(self.sub_stack) < self.capacity:
            self.sub_stack.append(value)
        else:
            self.stack.append(self.sub_stack)
            self.sub_stack = []
            self.sub_stack.append(value)

    def print_stack(self):
        if len(self.stack) > 0:
            if len(self.sub_stack) > 0:
                print(self.stack + self.sub_stack)
            else:
                print(self.stack)
        else:
            print(self.sub_stack)

    def pop(self):
        if len(self.sub_stack) > 0:
            self.sub_stack.pop()
        else:
            if self.count == self.capacity:
                self.i -= 1
                self.count = 0
            self.stack[self.i].pop()
            self.count += 1


s = Stack(5)
for i in range(20):
    s.push(i)
s.pop()
s.pop()
s.pop()
s.print_stack()
