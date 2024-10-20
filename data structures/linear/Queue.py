
Max = 12
class Queue:
    def __init__(self):
        self.rear = -1
        self.front = -1
        self.items = []
        self.Max = Max

    def insert(self, val):
        if self.rear == self.Max - 1:
            print("Overflow")
        else:
            if self.front == -1:
                self.front = 0
            else:
                self.rear += 1
                self.items.append(val)

    def print_queue(self):
        for c in self.items:
            print('%d' % c, end = ' ')

    def dequeue(self):
        if self.front == -1:
            print("Underflow")
            return -1
        else:
            top = self.items.pop(0)
            self.front += 1
            return top

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
print("Elements after enqueuing:")
q.print_queue()

print("\nElements after dequeue:")
q.dequeue()
q.dequeue()
q.print_queue()