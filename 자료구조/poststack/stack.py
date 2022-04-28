class stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    # self.top.pop(len(self.top)) 가능
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []
