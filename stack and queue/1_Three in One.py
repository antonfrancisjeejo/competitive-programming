class Stack:
    def __init__(self, n):
        self.array = [0] * n
        self.stack1 = 0
        self.stack2 = int(n / 3)
        self.stack3 = self.stack2 * 2
        self.print1 = self.stack1
        self.print2 = self.stack2
        self.print3 = self.stack3

    def push(self, stack_no, stack_value):
        if stack_no == 1:
            self.array[self.stack1] = stack_value
            self.stack1 += 1
        elif stack_no == 2:
            self.array[self.stack2] = stack_value
            self.stack2 += 1
        else:
            self.array[self.stack3] = stack_value
            self.stack3 += 1

    def pop(self, stack_no):
        if stack_no == 1:
            print(self.array[self.stack1 - 1])
            self.stack1 -= 1
        elif stack_no == 2:
            print(self.array[self.stack2 - 1])
            self.stack2 -= 1
        else:
            print(self.array[self.stack3 - 1])
            self.stack3 -= 1

    def print(self):
        print("Stack 1")
        for i in range(self.print1, self.stack1):
            print(self.array[i], end=" ")
        print("\nStack 2")
        for i in range(self.print2, self.stack2):
            print(self.array[i], end=" ")
        print("\nStack 3")
        for i in range(self.print3, self.stack3):
            print(self.array[i], end=" ")


s = Stack(30)
for value in range(1, 6):
    s.push(1, value)
for value in range(10, 16):
    s.push(2, value)
for value in range(20, 26):
    s.push(3, value)
s.print()
s.pop(1)
s.pop(2)
s.pop(3)
s.print()
