class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0 
    
    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()
    
    def Peek(self):
        return self.items[len(self.items)-1]
    
    def Size(self):
        return len(self.items)