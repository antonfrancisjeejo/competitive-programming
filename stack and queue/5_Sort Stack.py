class Stack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def top_stack(self):
        return self.stack[-1]

    def top_temp_stack(self):
        return self.temp_stack[-1]

    def push(self, value):
        self.stack.append(value)

    def push_temp_stack(self, value):
        self.temp_stack.append(value)

    def isEmpty_temp_stack(self):
        return len(self.temp_stack) == 0

    def isEmpty_stack(self):
        return len(self.stack) == 0

    def pop_stack(self):
        if (self.isEmpty_stack()):
            print("Stack Underflow ")
        return self.stack.pop()

    def pop_temp_stack(self):
        if (self.isEmpty_stack()):
            print("Stack Underflow ")
        return self.temp_stack.pop()

    def sortStack(self):
        while not self.isEmpty_stack():
            temp = self.top_stack()
            self.pop_stack()
            while (self.isEmpty_temp_stack() == False and
                   int(self.top_temp_stack()) > int(temp)):
                self.push(self.top_temp_stack())
                self.pop_temp_stack()
            self.push_temp_stack(temp)

    def prints(self):
        for i in range(len(self.temp_stack)):
            print(self.temp_stack[i], end=' ')
        print()


s = Stack()
s.push(54)
s.push(20)
s.push(60)
s.push(30)
s.push(2)
s.push(5)
s.sortStack()
s.prints()
