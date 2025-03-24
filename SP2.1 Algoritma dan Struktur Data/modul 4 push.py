class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
    def remove(self):
        if len(self.stack) <= 0:
            return ("Tidak ada elemen pada Stack")
        else:
            return self.stack.pop()
        
AStack = Stack()
AStack.add("senin")
AStack.add("selasa")
AStack.add("rabu")
AStack.add("kamis")
print(AStack.remove())
print(AStack.remove())