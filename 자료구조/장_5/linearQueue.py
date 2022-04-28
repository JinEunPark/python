class linearQueue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def peek(self):
        return self.list[-1]

    def dequeue(self):
        return self.list.pop(-1)

    def enqueue(self, item):
        self.list.insert(0, item)

    def size(self):
        return len(self.list)

    def clear(self):
        self.list = []
