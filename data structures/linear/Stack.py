

class Stack:
    def __init__(self):
        self.top = -1
        self.data = []
        self.MAX = 100

    def push(self, val):
        if self.top == self.MAX - 1:
            print("The stack is full")
        else:
            self.top += 1
            self.data.append(val)

    def pop(self):
        if self.top == -1:
            print("The stack is empty")
            return None
        else:
            val = self.data[self.top]
            self.data.pop()
            self.top -= 1
            return val

    def print_stack(self):
        for x in self.data:
            print("%d" % x, end = ' ')

    def peek(self):
        if self.top == -1:
            print("The stack is empty")
            return -1
        else:
            return self.data[self.top]

    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.MAX - 1

s = Stack()
print("Is the stack empty %d" % s.is_empty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()
print("\nThe top element of the stack is %d" % s.peek())
s.pop()
s.pop()
s.print_stack()
print("\nThe top element of the stack is %d" % s.peek())
print("Is the stack empty %d" % s.is_empty())


