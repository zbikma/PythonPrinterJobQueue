class Queue:
    def __init__(self):
        self.items=[]
    def AQueue(self,item):
        self.items.insert(0,item)
    def DQueue(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items==[]
