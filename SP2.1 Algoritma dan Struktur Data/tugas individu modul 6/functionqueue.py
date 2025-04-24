class Queue:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) >= self.max_size

    def Enqueue(self, item):
        if not self.isFull():
            self.items.insert(0, item)
            return True
        return False

    def Dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def Peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def Size(self):
        return len(self.items)

    def MaxSize(self):
        return self.max_size